---
aspects: 
tags: 
  - thing
  - actionable
  - visitor | resident
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

## Info

## Quotes