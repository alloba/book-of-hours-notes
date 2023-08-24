---
aspects: 
  - element of the soul: 1
  - occupant: 1
tags: 
  - soul
  - card
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