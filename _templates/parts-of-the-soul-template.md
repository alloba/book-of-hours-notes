---
aspects: 
  - name: 'element of the soul'
    amount : 1
  - name: occupant 
    amount: 1
tags: 
  - soul
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

### Normal 
### Fatigued
### Strained 

## Information