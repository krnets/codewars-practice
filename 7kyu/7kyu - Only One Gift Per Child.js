// 7kyu - Only One Gift Per Child

/* Santa is handing out gifts in the kindergarten. Many toddlers are around there and everyone should have 
the opportunity to have a seat on Santa's lap. But there's Peter, a 5 year old boy, who is a bit naughty. 
He tries to get two gifts. After he got the first one, he lines up again in the queue of children.

But fortunately Santa is not alone. His elves keep a list with the names of the children, which already were 
on Santa's lap. We know, that each child name is unique. If a child tries to get a second gift, the elves will tell Santa.

OK, let's help Santa and his elves with a simple function handOutGift() which takes the name of the next child. 
If this child already got a gift, it must throw an error in order to remind Santa.

handOutGift("Peter");
handOutGift("Alison");
handOutGift("John");
handOutGift("Maria");
handOutGift("Peter"); // <-- must throw an error */

let children = []

function handOutGift(name) {
    if (children.includes(name)) {
        throw new Error
    } else {
        children.push(name)
    }
}

q = handOutGift("Peter") // no error
q
q = handOutGift("Alison") // no error
q
q = handOutGift("John") // no error
q
q = handOutGift("Maria") // no error
q
q = handOutGift("Peter") // must throw an error
q