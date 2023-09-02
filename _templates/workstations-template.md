---
aspects: 
  - name: 
    amount: 1
slots: 
tags: 
  - workstation
challenges: 
 - "prentice-level challenges"
 - "scholar-level challenges"
 - "keeper-level challenges"
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