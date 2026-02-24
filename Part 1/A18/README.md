# Introduction
To complete this activity, I used the free version of ChatGPT using GPT-5.2 (the current model available for free users as of 23/02/2026) as it is the most popular LLM currently available. Consequently, it is also the most likely to hallucinate because it lacks features that other, more premium models have like thinking capabilities. In order to force the model to hallucinate, I tried various things and found that it hallucinated in very specific circumstances.

Note that the specific chats can be accessed by clicking on each heading for verification purposes.

## [Case 1](https://chatgpt.com/share/699c5cfa-a8b0-800b-870b-d807523412c9)
The first thing I tried which got the model to hallucinate was generating quotes from a bok, which it is notoriously awful at. In order to test this, I used the following prompt:
> Generate some quotes from Bram Stoker's 'Dracula' novel that showcase how Transylvania maintains conventions of the gothic genre.

This particular prompt was inspired by a previous assignment in which I wrote an essay on a similar topic for ATAR English in 2023. In order to check that the quotes were valid, I used the find command in my PDF viewer on a PDF copy of the book available [here](https://bramstoker.org/pdf/novels/05dracula.pdf) (the book was published in 1897 so it should be in the public domain). An example of this can be seen with the third quote, which I directly copied from the output:
![evidence](case1_q3.png)

The generated output was surprisingly coherent. It seemingly generated some quotes from the novel and explained their significance to my query in some level of detail (some of which isn't necessarily true, but checking the validity of such information would be much harder than some quotes). After inspecting every quote, there was one that stuck out:
> It is all superstition, and I fear you will smile at me; but you must promise me not to go out of your way. The things that have been will be again.

This is an interesting quote that appears to, on the surface, be an excellent quote for such an essay. However, this quote doesn't appear in the novel at all! There are exactly 0 instances in the novel in which this exact thing is said:
![evidence](case1_q2full.png)

Even after cutting this quote down in various ways (to the point I was looking at single words), there was nothing remotely close to this quote:
![evidence](case1_q2cut.png)

Consequently, this is one case where an LLM has hallucinated information.

## Case 2