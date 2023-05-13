^j::
Now := A_TickCount
While, (A_TickCount - Now) < 4000
{
	Send, {r Down}
	Sleep 30
}
send, {r Up}
Return