# Consumables
```dataviewjs
let items = dv.pages('"things"')
let valids = [
	'grail', 'winter', 'lantern', 'nectar', 'heart', 'knock',
	'sky', 'forge', 'moth', 'moon', 'scale', 'edge', 'rose',
	
]

let working_set = items
	.filter(x => x.aspects)
	.filter(x => x.aspects
				.map(y => y.name)
				.some(z => [
					'beverage', 'sustenance', 
					'tool', 'memory'
				].includes(z)) 
	)
let containsAspects = (item, valids) => {
	if(! item.aspects) return false
	return item.aspects.map(x => x.name).some(y => valids.includes(y))
}

dv.table(
	['Item', 'Aspects'],
	working_set
	.filter(x => containsAspects(x, valids))
	.map(x => 
	[
		x.file.link,
		x.aspects
			.filter(z => valids.includes(z.name))
			.map(z => z.name + ' ' + z.amount)
			.sort()
	]
	) 
)
```
