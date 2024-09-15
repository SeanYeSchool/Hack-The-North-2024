## Inspiration

Just Dance was probably my favorite game as a kid. Not only because I got to listen to Psy a million times a day, but because I loved to run and hop and dance around. At this hackathon, it was an inspiration for us to try and build something similar for everyone: a pose guiding app that helped people get active. 

## What it does

Yoga Yogi is the everyman’s yoga guide. Using pose recognition, Yoga Yogi recognizes your yoga poses and gives you individualized feedback on how to improve! Not only do we feature a login, you can design your very own yoga routine individualized to poses and duration goals. Once you are ready to start, Yoga Yogi will walk you through a guided yoga session, where you will receive live feedback and helpful tips.

## How we built it

Our project connected multiple moving parts, including a React frontend, a pose recognition model, and a Flask backend. 

Using Flask had huge importance in our project as it connected our Voiceflow and AI backend to our frontend React elements. Voiceflow was fun to use as it was very easy to create user help agents as well as AI responses specific for programmed API calls.

Collecting our data and training our model took several steps. To collect our data, we used mediapipe and cv2 to identify the major nodes of people in yoga poses and transformed these into graphs. We then used this dataset to train a graph neural network, which allowed us to classify pose images into distinct classes. Lastly, we used Voiceflow to generate customized feedback based on real time video. 


## Challenges we ran into

Since this was our first time working together collaboratively on Github, we struggled quite a lot with figuring out what merge meant and what branches were and whatever rebase meant. But after we got the hang of that, the next obstacle we faced was smoothly running the front and backend together, but not because of technical difficulties, but because of our difficulties with communicating with each other. All of us had unique skill sets, and we oftentimes struggled with communicating what our programs needed and outputted. This slowed us down a considerable amount, but despite this, we were able to make a project that was greater than our sum. 

## Accomplishments that we're proud of

Sean: Learning how to work together as a team as well as planning our time during the event and making smart compromises at the same time and still produce a functional project. Using API’s such as Convex and Voiceflow were also very interactive and a great learning experience.

Chris: I’m really happy with how simple and streamlined our UI is! It feels like a real app you would find online. This was the first time for me to work in a large group at a sprint pace, and although at some times I felt really tired, I really enjoyed my experience and would come again.

Steven: I am really happy with the learning progress I have made during the 36 hours. I had almost no experience coming in with web design and with using React and other frameworks. I was able to learn so much on the spot and reflecting on the past 2 days of work, I feel accomplished and thankful for this opportunity. I want to also thank my team members for helping me with so much and teaching me new pieces of coding knowledge that I would not have known.

Nirvan: I am very proud of the team effort and collaboration that we had the entire time. We worked really hard and supported each other whenever we had an error particularly those between the react frontend and flask backend. I am particularly proud of overcoming the issue of having multiple setIntervals in different components by passing props to a parent component and having one common useEffect to run all the setIntervals.

## What we learned

A lot of front end and APIs! While the more technical parts are usually documented thoroughly, making a clean and satisfying frontend that we liked was much more creatively difficult than we thought. We each all had our own different thoughts and ideas about what we liked and what we wanted to put in, but making a project we were all proud of meant that we had to compromise on things that we didn’t want.

## Visit our Devpost
https://devpost.com/software/yoga-yogi

## What's next for Yoga Yogi

We want to put Yoga Yogi on phones! This would allow Yoga Yogi to guide you through his practices, anytime, and anywhere. We also want to train Yoga Yogi on more poses, allowing Yoga Yogi to give you step by step feedback rather than broader statements. 
