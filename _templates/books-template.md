---
aspects: 
  - codex: 1
  - thing: 1
tags: 
  - book
  - actionable
lesson: 
memory: 
---

<%*
let filename = tp.file.title
if ( filename.startsWith("Untitled") ) {
  filename = await tp.system.prompt("File name: ")
  await tp.file.rename(filename)
} 
tR += `# ${filename}`
%>

## Description

### Partial Study Description

### Study Complete Description
