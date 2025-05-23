const fs = require('fs');
const path = require('path');

const IGNORE_DIRS = ['node_modules', '.git', '__pycache__', '.idea', '.vscode'];
const OUTPUT_FILE = 'all_code_output.txt';
const ROOT_DIR = process.cwd();

function walkDir(dir, callback) {
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    if (IGNORE_DIRS.includes(file)) return;

    if (fs.statSync(fullPath).isDirectory()) {
      walkDir(fullPath, callback);
    } else {
      callback(fullPath);
    }
  });
}

function exportFiles() {
  const writeStream = fs.createWriteStream(OUTPUT_FILE, { flags: 'w' });

  walkDir(ROOT_DIR, (filePath) => {
    try {
      const content = fs.readFileSync(filePath, 'utf-8');
      const relativePath = path.relative(ROOT_DIR, filePath);

      writeStream.write(`\n--- FILE: ${relativePath} ---\n`);
      writeStream.write(content + '\n');
    } catch (err) {
      console.error(`Failed to read file: ${filePath}`, err);
    }
  });

  writeStream.end(() => {
    console.log(`✅ All files exported to ${OUTPUT_FILE}`);
  });
}

exportFiles();
