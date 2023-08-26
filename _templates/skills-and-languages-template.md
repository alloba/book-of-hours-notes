---
aspects: 
  - name: skill
    amount: 1
tags: 
  - skill
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

## Tree of Wisdom Entries