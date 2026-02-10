import re
import sys
from pathlib import Path
import tarfile

def test_notes(notes_path: Path):
    with notes_path.open("r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        
    answers = {}
    task_re = re.compile(r"^(Task\s+\d+\.\d+)", re.IGNORECASE)
    letter_re = re.compile(r"^\(([a-z])\)", re.IGNORECASE)
    current_task, current_part = None, None

    for line in lines:
        line_stripped = line.strip()
        task_match = task_re.match(line_stripped)
        if task_match:
            current_task = task_match.group(1)
            answers[current_task] = {}
            current_part = None
            continue

        part_match = letter_re.match(line_stripped)
        if part_match and current_task:
            current_part = part_match.group(1).lower()
            answers[current_task][current_part] = []
            continue

        if current_task and current_part:
            answers[current_task][current_part].append(line_stripped)

    for task, parts in answers.items():
        for part, text_lines in parts.items():
            answers[task][part] = "\n".join(text_lines).strip()

    return answers



def marking_criteria(answers):
    marks_total = 0

    def get(task, part):
        return answers.get(task, {}).get(part, "")

    # Task 1.1a
    ab = get("Task 1.1", "a") + get("Task 1.1", "b")
    for needle in [
        "import pip", # sdist
        "pip.main(['install', 'mattyt'])", # sdist
        "install_requires", # bdist
        "mattyt", # bdist
    ]:  
        if needle in ab:
            marks_total += 1
            
    # Task 2 bonus (5 marks)
    # Task 2.1
    a = get("Task 2.1", "a")
    if 'pip install' in a and 'git+https://github.com/psf/requests.git' in a:
        marks_total += 1

    if "index-url" in get("Task 2.1", "b"):
        marks_total += 1

    if "--no-deps" in get("Task 2.1", "c"):
        marks_total += 1

    # Task 2.2f
    if "uv.lock dependencies for vulnerabilities" in get("Task 2.2", "f"):
        marks_total += 2

    # Task 3.1a
    a = get("Task 3.1", "a")
    parts = [p.strip() for p in re.split(r'- tool \d+:\s*', a) if p.strip()]
    if len(parts) == 4:
        marks_total += sum(
            2 for ans in parts if ans != "# Your answer here" and len(ans) > 3
        )

    # Task 3.2
    ab = get("Task 3.2", "a") + get("Task 3.2", "b")
    if "https://github.com/MatthewAndreTaylor/supply-chain-vulnerabilities/actions/runs/21366800325/artifacts/5260264315" in ab:
        marks_total += 1
    if "Setup stuff" in ab:
        marks_total += 1

    return marks_total

        

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <folder>")
        sys.exit(1)

    folder = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"Error: {folder} is not a directory")
        sys.exit(1)

    notes = folder / "notes.txt"
    pyproject = folder / "pyproject.toml"
    uv_lock = folder / "uv.lock"
    tarballs = list(folder.glob("awesome_mathutils-*.tar.gz"))
    tarball = tarballs[0] if tarballs else None
    
    marks = 0
    
    # 3. If notes.txt exists, run some custom lint/check
    if notes.exists():
        marks += marking_criteria(test_notes(notes))

    if pyproject.exists() and uv_lock.exists():
        # student recieves bonus marks for doing the bonus task
        marks += 3
        
    includes_package_data = False

    # 2. If sdist tarball exists, run packaging validation
    if tarball and tarball.exists():
        with tarfile.open(tarball, "r:gz") as tar:
            for member in tar.getmembers():
                if member.name.endswith("setup.py"):
                    marks += 2
                    f = tar.extractfile(member)
                    if f:
                        content = f.read().decode("utf-8")
                        if "include_package_data" in content:
                            includes_package_data = True
                if member.name.endswith("pyproject.toml"):
                    marks += 2
                    f = tar.extractfile(member)
                    if f:
                        content = f.read().decode("utf-8")
                        if "build-backend" in content and "setuptools.build_meta" in content:
                            marks += 2
                            
                        if "include-package-data" in content:
                            includes_package_data = True
                if member.name.endswith(".bmp"):
                    marks += 1

            
    if includes_package_data:
        marks += 2
    
    
    total_marks_threshold = 11
    
    # There are 32 marks available in total, 23 without bonus
    # We are very lenient in this autograder anything above total_marks_threshold=11 is 100%
    percentage = min(100, (marks / total_marks_threshold) * 100)
    print(f"Total Marks: {marks}/{total_marks_threshold} ({percentage:.2f}%)")    
    


if __name__ == "__main__":
    main()
