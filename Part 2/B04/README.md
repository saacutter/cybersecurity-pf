# Introduction
To complete this activity, I attended 3 different labs - March 12, April 2, and April 23. These each covered different topics from the previous week's lecture, like encryption, security tools, and intrusion detection systems. For each activity, I have provided varied evidence which should prove completion.

## Activity 1 - Thursday, March 12 (Week 3)
For this activity, everyone got into groups of 4-5. Each person came up with a random number (which for me was whatever number came to my head first, which was 148), and the goal was to calculate the average of every person's number without anyone finding out anyone else's chosen number.

Initially, we tried formatting the number in some way with some calculation (i.e. multiplying/dividing/adding/subtracting by an arbitrary amount) and writing it on a list as an "encrypted" number (for this, I just halved my number resulting in an "encrypted" number of 74). Then, each person could average the numbers written, using their actual numbers instead of their "encrypted" numbers once they got to that position in the list. Once everyone had an average, each person could say their average and then the average of the averages calculated. The thought process behind this would be that the "encrypted" numbers would be averaged out of the equation, with only each person's numbers left. This, however, did not work so we tried to come up with another solution.

The next attempt we instead decided to split our numbers up into 3 components (where all 3 add up to our numbers), write these on a piece of paper, and transfer it to the 3 people on our left (because by this point, the group's size had grown to 7 people). The totals each person had could then be written down, and the average of each person's sum could be calculated. This should have worked in theory, but with the amount of people in the group it did not end up working too well (although, according to the lab facilitator it was really close).

The group was then split into 2 to try and limit mistakes due to the amount of people. This same process was done, but instead of splitting the number up into 3 pieces it was instead split into 2. These pieces were then written down on pieces of paper, and a piece given to the two people on our lefts. Each person then calculated the sum of the numbers they were given, and the average of the sums was calculated. This finally gave us the correct average, with a result of 67.5 (the only number I am aware of in this sum was my number, but from this result it could very well have been the maximum).

Evidence for this activity was hard to get. Taking photos of the pieces of paper would not realistically prove anything, nor would taking a photo of me in the room. This write-up is intended to act as evidence, as it would be impossible to know what happened in the lab nor write about a process without having attended this lab.

<br>

## Activity 2 - Thursday, April 2 (Week 6)
For this activity, everyone split into groups of 3 (though my group had 4 due to the number of people). The task was website vulnerability scanning, and then reporting our findings to the group. To do this, I used the Docker image of OWASP ZAP and scanned http://demo.testfire.net. I then used the results of this to discuss with the other group members.

The evidence provided is a photo taken by one of the group members, as well as a photo of me using OWSAP ZAP.

<br>

## Activity 3 - Thursday, April 23 (Week 8)
This activity was focused on intrusion detection systems, specifically focusing on anomaly-based systems. Although this activity required everyone to split into groups of 4, the lab initially only had 3 people so we acted as a group of 3 (with the lab facilitator acting as the fourth). This activity used playing cards acting as network traffic, with one person acting as the network putting the deck of cards down in quick succession. The other people had to try and filter the traffic by looking at the card and grabbing it from the pile if it was marked "malicious" (with a reference provided by the facilitator) before the next one could be put down. When all the cards were put down, the cards which were grabbed from the pile were pooled to identify the number of true positives, true negatives, false negatives, and false positives.

A total of three attempts of this activity were made. None of these attempts were particularly successful, but some of the malicious "traffic" was pulled out with only a few false positives and false negatives.

The evidence for this activity is the initial outcome of the cards I pulled from the pile, as well as a photo of the malicious card reference list.