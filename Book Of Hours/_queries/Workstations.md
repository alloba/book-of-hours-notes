
# Workstations that Evolve
```dataviewjs
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

let working_set_things = dv.pages('"Book Of Hours/things"')
let working_set_workstations = dv.pages('"Book Of Hours/workstations"')


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