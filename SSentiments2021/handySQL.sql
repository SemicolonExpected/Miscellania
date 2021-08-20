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
