on run argv
	set calName to item 1 of argv
	set sy to (item 2 of argv) as integer
	set sm to (item 3 of argv) as integer
	set sd to (item 4 of argv) as integer
	set ey to (item 5 of argv) as integer
	set em to (item 6 of argv) as integer
	set ed to (item 7 of argv) as integer
	
	set startDate to current date
	set day of startDate to 1
	set year of startDate to sy
	set month of startDate to sm
	set day of startDate to sd
	set time of startDate to 0
	
	set endDate to current date
	set day of endDate to 1
	set year of endDate to ey
	set month of endDate to em
	set day of endDate to ed
	set time of endDate to (23 * 3600 + 59 * 60 + 59)
	
	set output to ""
	
	tell application "Calendar"
		try
			set targetCal to calendar calName
			set targetEvents to (every event of targetCal whose start date ≥ startDate and end date ≤ endDate)
			
			repeat with ev in targetEvents
				set evTitle to summary of ev
				set evStart to start date of ev
				set evEnd to end date of ev
				
				set output to output & calName & "|||" & evTitle & "|||" & (evStart as string) & "|||" & (evEnd as string) & "\n"
			end repeat
		on error errMsg
			-- 如果报错，把错误信息伪装成一条记录返回
			return calName & "|||🚨 系统报错: " & errMsg & "|||检查|||权限\n"
		end try
	end tell
	
	return output
end run