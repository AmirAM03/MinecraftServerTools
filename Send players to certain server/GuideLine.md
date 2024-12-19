# Guideline for Player Transfer Tools

This directory contains tools developed to transfer a specified list of online players from a proxy server to a designated backend server. 

During the project, my primary stack involved working with **Velocity** and **BungeeCord** proxy servers. To accomplish this, I utilized the internal `send` command provided by these proxy servers. Several tools have been created for this purpose, all of which you can find in this directory.

---

## Tool: Command Generator

### Purpose

This tool is designed for scenarios where you have access to the proxy server's **Server Software Console**. One of the most common approaches is to input the following command for each player:

```bash
/send username servername
```

This tool automates the process by:
1. Reading a list of usernames from a `users.txt` file (one username per line).
2. Generating equivalent `send` commands for all usernames.
3. Writing these commands to a `Commands.txt` file.

You can then execute the commands in the proxy server's console by any means.

---

## Tool: Clipboard Command Generator

### Purpose

This tool is a variation of the **Command Generator** with the following differences:

- Instead of saving the generated commands to a file, it stores them in your system's clipboard using the `pyperclip` library.
- This allows you to paste all the commands directly into the proxy server's console, simplifying the execution process.

### Installation

Before using this tool, install the `pyperclip` library:

```bash
pip install pyperclip
```

### Usage

1. Run the tool to generate and copy the commands to your clipboard.
2. Paste the clipboard content into the proxy server's console. For systems with a GUI-based SSH interface, this can typically be done with a simple right-click.

### Handling Execution Speed Issues

When using Velocity or BungeeCord, pasting a series of `send` commands in quick succession can sometimes lead to commands being blocked by the proxy server due to the high execution speed. To resolve this:

- The tool accepts an integer variable, `extra_newlines_count`, which adds empty newlines after each command in the clipboard content.
- These extra newlines create an artificial delay when all commands are pasted at once, preventing the proxy server from blocking them.

**Note:** A similar feature can be implemented for the **Command Generator** if needed.

---

## Tool: Spread Sheet Reader

### Purpose

The most significant bottleneck in this automation process is collecting and efficiently managing the in-game usernames of players to be included in the `users.txt` file. 

This largely depends on your project's setup and how player data is maintained. In my case, a **Google Spreadsheet** was used. To address this, I developed the **Spread Sheet Reader** tool. 

### How It Works

1. The tool accepts a list of team names as input.
2. For each team name, it retrieves the names of all players mapped to that team in the Google Spreadsheet.
3. It writes the collected player names to the `users.txt` file.
4. Using Python's `subprocess` library, it automatically executes the required script with the generated `users.txt` file.

This tool streamlines the process and eliminates the manual effort of gathering player usernames.

---

## Summary

These tools are designed to:
- Automate the repetitive process of sending players to backend servers.
- Enhance efficiency by reducing manual input.
- Provide customizable solutions for specific project needs, including handling execution speed limitations.

Feel free to explore the code and adapt it for your specific requirements.

---

## Persian Desc

<div dir="rtl" align="right">
این ابزار با این هدف بوجود آمده که لیست مشخصی از بازیکنان را (که طبیعتا بایستی در سرور آنلاین باشند) از طریق پروکسی سرور به BackendServer معینی ارسال کند

از آنجا که استک کاری من در طول پروژه مربوطه کار با پروکسی سرور Velocity و BungeeCord بوده است من این عملیات را بوسیله استفاده از دستور داخلی send این دو پروکسی سرور انجام میدادم به همین دلیل ابزارهای متعددی بدین منظور ایجاد شده که در این دایرکتوری میتوانید هرکدام را مشاهده کنید



### ابزار Command Generator
این ابزار برای شرایط زیر طراحی شده :
فرض کنید شما به کنسول Server Software پروکسی سرور دسترسی دارید ، یکی از معمول ترین ایده ها این است که به تعداد هر کدام از بازیکنان دستور
</div>

```bash
/send username servername
```

<div dir="rtl" align="right">

را در کنسول وارد کنید
برای این منظور این ابزار لیست یوزرهای مدنظر را که بصورت line separated در فایل users.txt قرار گرفته اند خوانده و دستورات send معادل با تمامی یوزرهارا در فایل Commands.txt برای شما ایجاد میکند که کافی ست به هر طریقی این دستورات را در کنسول پروکسی سرور اجرا کنید

</div>
<div dir="rtl" align="right">

### ابزار Clipboard Command Generator

این دقیقا همان ابزار قبلی ست با این تفاوت که تمامی دستورات را در کلیپ بورد سیستم شما ذخیره میکند و این کار را از طریق کتابخانه pyperclip انجام میدهد که بایستی آنرا از طریق دستور
pip install pyperclip
نصب کنید
پس از یکمرتبه اجرای این دستور کافی محتویات کلیپ یورد خود را در کنسول پروکسی سرور Paste کنید که اصولا این عمل در رابط های کاربری SSH سیستم عامل های دارای GUI بسیار ساده انجام میشود و تمامی آن پروسه سخت را برای من به یک کلیک راست خلاصه میکرد :)


یک چالش مهم در رابطه با استفاده این رویکرد برای Velocity و BungeeCord این است که در صورتیکه مثلا ابزار دوم را استفاده کنید و تمام محتویات کلیپ بورد بصورت یکسری Line پشت سرهم که هر خط شامل دستور ارسال یک بازیکن است را در کنسول پروکسی سرور Paste کنید بدلیل سرعت بالای اجرای دستورات پشت سر هم برخی دستورات توسط نرم افزار پروکسی سرور بلاک خواهند شد، برای رفع این مشکل ابزار دوم یک عدد صحیح در قالب متغیر "extra_newlines_count" دریافت میکند و به ازای هر دستور ارسال به تعداد این عدد empty new line به محتوای کلیپ بورد الصاق میکند و این باعث ایجاد یک delay مصنوعی حین Paste کردن تمامی دستورات باهم و همزمان در کنسول میشود که مشکل را رفع میکند

واضحا میتوان مشابه این کار را برای ابزار اول انجام داد



### ابزار Spread Sheet Reader

و اما تنها بخش Bottleneck این پروسه Automation بحث جمع آوری و مدیریت بهینه in-game username بازیکنانی ست که بایستی در فایل users.txt قرار گیرد

خب این کاملا به شرایط و وضعیت پروژه شما و نحوه مدیریت و نگهداری داده های بازیکنان وابسته ست که بصورت خاص برای من یک Google SpreadSheet پس بدین منظور من ابزار سوم را نوشتم که مبتنی بر دریافت یکسری Team Name (که در Spread Sheet هر TeamName به اسم 5 بازیکن Map شده است) اسامی تمام بازیکنان هر تیم را از شیت مربوطه خوانده و در فایل users.txt میریخت و در ادمه بوسیله کتابخانه subprocess در پایتون فایل مورد نیاز را اجرا میکرد


</div>