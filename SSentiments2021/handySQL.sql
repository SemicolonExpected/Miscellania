#select number of partial responses


#get a matrix of demographics to responses

#age vs responses

#undergrad vs gradschool vs responses


#get count of degrees persuing
SELECT degreePersuing, count(degreePersuing)
from data
GROUP BY degreePersuing;

#get count of degree/year in degree
SELECT degreePersuing, yearInProgram, count(yearInProgram)
from data
GROUP BY degreePersuing, yearInProgram;

#count of people who used each software and people who didnt
SELECT ifZoomUsed, COUNT(ifZoomUsed) as countUsed
FROM data
GROUP BY ifZoomUsed;

SELECT ifLMSUsed, COUNT(ifLMSUsed) as countUsed
FROM data
GROUP BY ifLMSUsed;

# get software used
SELECT VidConSoftwareUsed, count(VidConSoftwareUsed)
FROM data
Group BY VidConSoftwareUsed;

SELECT LMSUsed, count(LMSUsed)
FROM data
WHERE ifLMSUsed = 'Yes'
Group BY LMSUsed;

SELECT ProctorUsed, count(ProctorUsed)
FROM data
WHERE ifProctorUsed = 'I have used a proctoring software'
Group BY ProctorUsed;

# of people who had mandatory camera given their desire for recording
# P(mandatoryCamera|recordingdesire)

SELECT data.ifWantRecording, ifMandatoryCamera, c, COUNT(data.ifMandatoryCamera) as countDistinct, CAST(COUNT(data.ifWantRecording) as float)/c*100 as percentage
FROM data, (SELECT ifWantRecording, COUNT(ifWantRecording) as c FROM data GROUP BY ifWantRecording) as d
WHERE data.ifWantRecording = d.ifWantRecording
GROUP BY data.ifWantRecording, ifMandatoryCamera;

# of people who wanted recording given mandatory camera status
# P(recordingDesire|mandatorycamera)
SELECT data.ifMandatoryCamera, ifWantRecording, c, COUNT(data.ifWantRecording) as countDistinct, CAST(COUNT(data.ifMandatoryCamera) as float)/c*100 as percentage
FROM data, (SELECT ifMandatoryCamera, COUNT(ifMandatoryCamera) as c FROM data GROUP BY ifMandatoryCamera) as d
WHERE data.ifMandatoryCamera = d.ifMandatoryCamera
GROUP BY data.ifMandatoryCamera, ifWantRecording;

# of people who answered a certain way in a proctoring likert given whether they have used/heard of a proctor
SELECT data.ifProctorUsed, ifComfortableProctor, c, COUNT(data.ifComfortableProctor) as countDistinct, CAST(COUNT(data.ifComfortableProctor) as float)/c*100 as percentage
FROM data, (SELECT ifProctorUsed, COUNT(ifProctorUsed) as c FROM data GROUP BY ifProctorUsed) as d
WHERE data.ifProctorUsed = d.ifProctorUsed
GROUP BY data.ifProctorUsed, ifComfortableProctor;

SELECT data.ifProctorUsed, ifPreferProctor, c, COUNT(data.ifPreferProctor) as countDistinct, CAST(COUNT(data.ifPreferProctor) as float)/c*100 as percentage
FROM data, (SELECT ifProctorUsed, COUNT(ifProctorUsed) as c FROM data GROUP BY ifProctorUsed) as d
WHERE data.ifProctorUsed = d.ifProctorUsed
GROUP BY data.ifProctorUsed, ifPreferProctor;

SELECT data.ifProctorUsed, ifBelieveFairProctor, c, COUNT(data.ifBelieveFairProctor) as countDistinct, CAST(COUNT(data.ifBelieveFairProctor) as float)/c*100 as percentage
FROM data, (SELECT ifProctorUsed, COUNT(ifProctorUsed) as c FROM data GROUP BY ifProctorUsed) as d
WHERE data.ifProctorUsed = d.ifProctorUsed
GROUP BY data.ifProctorUsed, ifBelieveFairProctor;

SELECT data.ifProctorUsed, ifBelieveEffectiveProctor, c, COUNT(data.ifBelieveEffectiveProctor) as countDistinct, CAST(COUNT(data.ifBelieveEffectiveProctor) as float)/c*100 as percentage
FROM data, (SELECT ifProctorUsed, COUNT(ifProctorUsed) as c FROM data GROUP BY ifProctorUsed) as d
WHERE data.ifProctorUsed = d.ifProctorUsed
GROUP BY data.ifProctorUsed, ifBelieveEffectiveProctor;
