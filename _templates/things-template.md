---
aspects: 
  - name: thing
    amount : 1
tags: 
  - thing
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

## Locations