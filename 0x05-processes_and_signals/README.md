PROJECT: 0x05. Processes and signals
DevOps Shell Bash Syscall Scripting
By: Sylvain Kalache
Project will start Sep 29, 2023 6:00 AM, must end by Sep 30, 2023 6:00 AM

TASKS
TASK: 0. What is my PID
mandatory
Write a Bash script that displays its own PID.

TASK: 1. List your processes
mandatory
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy

TASK: 2. Show your Bash PID
mandatory
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

TASK: 3. Show your Bash PID made easy
mandatory
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

You cannot use ps

TASK: 4. To infinity and beyond
mandatory
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

In between each iteration of the loop, add a sleep 2

TASK: 5. Don't stop me now!
mandatory
We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

You must use kill
Terminal #0

TASK: 6. Stop me if you can
mandatory
Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:

You cannot use kill or killall
Terminal #0

TASK: 7. Highlander
mandatory
Write a Bash script that displays:

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

Terminal #0

TASK: 8. Beheaded process
mandatory
Write a Bash script that kills the process 7-highlander.

Terminal #08. Beheaded process
mandatory
Write a Bash script that kills the process 7-highlander.

Terminal #0



