tell application "Calendar"

	set calendarNames to {}

	repeat with c in calendars
		copy (name of c) to end of calendarNames
	end repeat

	set AppleScript's text item delimiters to ","

	return calendarNames as text

end tell