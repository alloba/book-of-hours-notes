# Various
```dataviewjs
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}



let working_set = dv.pages('"things"')


dv.table(
	['Item', 'Aspects'],
	working_set
	.filter(x => x.aspects)
	.filter(x => containsAspects(x, ['tool']))
	.map(x => 
	[
		x.file.link,
		x.aspects.map(z => z.name + ' ' + z.amount),
	]
	) 
)
```



# Workstations that Evolve
```dataviewjs
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

let working_set_things = dv.pages('"things"')
let working_set_workstations = dv.pages('"workstations"')


dv.table(
	['Item', 'Evolve', 'Aspects', 'Slots'],
	working_set_workstations
	.filter(x => x.challenges)
	//.filter(x => 
	//	x.challenges.some(z => z.startsWith('evolve'))
	//)
	.map(x => 
	[
		x.file.link,
		x.challenges.filter(z=>z.startsWith('evolve')),
		x.aspects.map(z => z.name + ' ' + z.amount),
		x.slots
	]
	) 
)
```
