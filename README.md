#readme
<h1 align="center"> 𓆩༺ "Mephisto" the mechanical crow ༻𓆪 </h1>
 
<p align="center">
  🖤 A little interactive Discord bot, centered around Sylus from the game <em>Love & Deepspace</em>. 🐦‍⬛ <br>
  Coded entirely in Python, with a lot of caws.
</p>
<hr>
<h2> 𓆩「 What he does <em>for now</em> 」𓆪 </h2>
 
<ul>
  <li>✦ Responds to character-related triggers ⟡</li>
  <li>✦ Random positive affirmations when you need comfort ⟡</li>
  <li>✦ Makes fun bubble wrap to pop ⟡</li>
  <li>✦ Tells kitten jokes, crow jokes, and the occasional joke from Sylus himself ⟡</li>
  <li>✦ Daily water reminder and weekly stamina reminder ⟡</li>
  <li>✦ Daily game server reset reminders (Asia, Europe, America) ⟡</li>
  <li>✦ Welcome messages for new members ⟡</li>
  <li>✦ Keeps stats per server and gives a status report with <code>$mephisto</code> ⟡</li>
  <li>✦ Works on several servers, each with its own configuration ⟡</li>
</ul>
<hr>

<h2> 𓆩「 Configure him 」𓆪 </h2>
 
<p>All the slash commands live under <code>/config</code> and require the <strong>Manage Server</strong> permission. Answers are only visible to you.</p>
<ul>
  <li>✦ <code>/config channel</code> – choose a channel for <em>welcome</em>, <em>general</em>, <em>daily</em> or <em>weekly</em> ⟡</li>
  <li>✦ <code>/config role</code> – choose the role to ping for the weekly reminder ⟡</li>
  <li>✦ <code>/config welcome</code> – turn welcome messages on or off ⟡</li>
  <li>✦ <code>/config reset-reminder</code> – set a daily server reset reminder for a region (with an optional role to ping) ⟡</li>
  <li>✦ <code>/config unset-channel</code>, <code>unset-role</code>, <code>unset-reset-reminder</code> – remove a setting ⟡</li>
  <li>✦ <code>/config show</code> – recap of the current configuration ⟡</li>
</ul>
<p>Reminders are only sent in the channels you configured, so nothing happens until you set them up.</p>
<hr>
<h2> 𓆩「 Behind the feathers 」𓆪 </h2>
 
<ul>
  <li>✦ <strong>Python</strong> + <strong>discord.py</strong> ⟡</li>
  <li>✦ <strong>PostgreSQL</strong> (<code>asyncpg</code>) for the serious stuff: servers, channels, roles and reminders ⟡</li>
  <li>✦ <strong>MongoDB</strong> (<code>pymongo</code>) for the fun stuff: per-server stats ⟡</li>
  <li>✦ If MongoDB ever breaks, the bot keeps working, he just stops counting ⟡</li>
  <li>✦ Removing the bot from a server deletes all of that server's data ⟡</li>
</ul>
<pre>
Mephisto/
├─ database/
│  ├─ mongodb.py        stats (MongoDB)
│  ├─ postgres.py       servers, channels, roles, reminders
│  └─ schema.sql        PostgreSQL tables
├─ service/
│  ├─ config_service.py logic behind /config
│  └─ stats_service.py  counters and the $mephisto report
├─ bot.py               startup, database init, command sync
├─ commands.py          slash commands
├─ handler.py           join / leave / welcome / messages
├─ triggers.py          all the cute reactions
├─ games.py             bubble wrap
├─ reminders.py         scheduled reminders
└─ crowkittenjokes.json the joke list
</pre>
 
<hr>
<h2> 𓆩「 Summon your own Mephisto 」𓆪 </h2>
 
<p>If you'd rather host him yourself:</p>
<ol>
  <li>Create a bot in the <a href="https://discord.com/developers/applications">Discord Developer Portal</a> and enable the <strong>Message Content</strong> and <strong>Server Members</strong> intents.</li>
  <li>Create a PostgreSQL database and run <code>database/schema.sql</code>.</li>
  <li>Create a MongoDB cluster for the stats.</li>
  <li>Copy <code>.env.example</code> to <code>.env</code> and fill it in:</li>
  <li>Install the dependencies and wake him up:</li>
</ol>
bash: <code>
pip install -r requirements.txt
python bot.py
</code>
 
<p>Give him the permission to send messages in the channels you pick, or else... 🐦‍⬛</p>
<hr>
<h2> 𓆩「 What Next? 」𓆪 </h2>
 
<ul>
  <li>✦ Embedded Mephisto dress up game (or other js minigames) </li>
  <li>✦ Birthday reminders with user inputs </li>
  <li>✦ Random draws for raffles and giveaways </li>
  <li>✦ Custom UI for custom announcements/welcome </li>
  <li>✦ More lines for <code>play boss.mp3</code> </li>
</ul>
<br>
<p align="center">
  ☽ If you want to use the bot, please contact me, I'll gladly help you! ☾
</p>
<hr>
<p align="center">𓅪 ⌖</p>
