---
aspects: 
  - name: codex
    amount: 1
  - name: thing
    amount : 1
  - name: readable
    amount : 1
  - name: "tally price"
    amount : 1
  - name: "mystery: "
    amount : 1
tags: 
  - book
  - actionable
lesson: 
  - "lesson: "
memory: 
  - "memory: "
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
