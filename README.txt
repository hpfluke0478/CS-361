Requesting data: In SimpleMicro.py, the 'Notepad Directory' queue is declared to then consume contents within the body of callback. Once called,
		 callback appends the contents of body (I,e. the note entered by the user) to the 'notes' array for later access.

Receiving data: Data is received in 2 cases by the microservice. 

	Case 1: call getNote
		Once called, getnote sends the contents of the 'makeNote' textbox to the body of callback for storage.
	Case 2 - Special Case: call importNote (Unfinished, tips appreciated)
		Once called, get note should request the contents of 'notes' from SimpleMicro.py via basic_consume() and print them line by line to 'showNotes.'

Video Link: https://media.oregonstate.edu/media/t/1_lymx51an
