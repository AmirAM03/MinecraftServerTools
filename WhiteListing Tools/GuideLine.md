# Guideline for Whitelist Manager Tool with Telegram Integration

## Tool: Whitelist Manager

### Purpose

This tool is built on the **VelocityCoolList** plugin for the **Velocity** proxy server to automate the whitelisting process. While the implementation is specific to this plugin, the concept and approach can be adapted for other technologies.

The **VelocityCoolList** plugin identifies and manages the whitelist via a JSON file containing a simple JSON array of in-game usernames. To update the whitelist:
1. Modify the JSON file.
2. Execute the `/vcl reload` command in the proxy server console to reload the player list.

### Project Requirements

In my project, I needed to:
- Periodically whitelist specific usernames and clear the previous entries.
- Ensure certain staff members always remained on the whitelist.

To achieve this, the tool processes two input files:
- **Permanent.txt**: Contains usernames that must always be on the whitelist.
- **Temp.txt**: Contains usernames to be temporarily whitelisted.

The tool:
1. Reads usernames from both files.
2. Merges them into a JSON array formatted for the `whitelist.json` file.
3. Transfers the updated `whitelist.json` to the server using `scp`.
4. Executes `/vcl reload` on the proxy server to apply changes.

#### Addressing Bottlenecks

As with the **Send Players** tool, collecting and managing usernames was a bottleneck. In my case, usernames were retrieved from a **Google Sheet**. The directory includes an automated data-reading tool for this purpose, which will be further integrated in future commits.

---

## Telegram Bot Integration

To simplify username management, particularly for team members, I integrated the tool with a Telegram bot. This integration leverages Telegram's popularity as a social platform in my region.

### How It Works

- The `telegramintegrated.py` script in this directory deploys a Telegram bot.
- The bot:
  1. Accepts your bot token to initialize.
  2. Receives `Temp Whitelist` usernames as a line-separated message.
  3. Generates the `whitelist.json` file in the directory.
  4. Transfers the file to the Minecraft server using `scp`.

### Requirements

- **Bot Token**: You need to provide your Telegram bot token.
- **SSH Credentials**: The bot requires your server's SSH credentials to transfer the `whitelist.json` file.
- **Secondary Server**: The Telegram bot runs on a secondary server for hosting, ensuring the main server remains unaffected.

### Setup Instructions

1. Deploy the `telegramintegrated.py` script on a secondary server.
2. Configure the bot with your Telegram bot token and SSH credentials.
3. Run the bot.
4. Send usernames in a line-separated format to the bot on Telegram.

The bot will:
- Generate `whitelist.json`.
- Transfer it to your Minecraft server.
- Notify you once the process is complete.

### Advantages

- Simplifies whitelist management for team members.
- Provides a user-friendly interface via Telegram.
- Separates hosting of the bot from the main server, ensuring stability and security.

---

### Preprocessing Invalid Usernames

The tool includes preprocessing functions to clean invalid usernames using common approaches, such as removing whitespace characters (since Minecraft usernames cannot contain spaces). While these cleaning mechanisms exist in the main program, it is expected that the username list you use with this tool has already been preprocessed, or in other words, "Pre-Processed Data" should be provided.

---

## Summary

The **Whitelist Manager Tool with Telegram Integration** is designed to:
- Automate and streamline the whitelisting process for Minecraft servers.
- Integrate seamlessly with Telegram for ease of use.
- Leverage secondary server hosting for stability and security.

Feel free to explore, adapt, and extend the code to suit your specific needs.


---

# Persian Desc

<div dir="rtl" align="right">

## ابزار Whitelist Manager

در ابتدا باید اشاره کنم که این ابزار مبتنی بر روند Whitelisting پلاگین VelocityCoolList برای پروکسی سرور Velocity توسعه داده شده
با این حال همانطور که اشاره شد اگر شما از تکنولوژی متفاوتی استفاده میکنید حداقل میتوانید ایده های مشابهی را پیاده سازی کنید یا ابزار موجود در این ریپوزیتوری را ویرایش کنید


مکانیزم عملکردی پلاگین مذکور به این صورت است که جهت تشخیص و مدیریت Whitelist فعلی سرور یک فایل json که شامل یک json array ساده میباشد را که داخل آن in-game username بازیکنان ذخیره شده نگهداری میکند به همین دلیل تنها نیاز ما برای اعمال تغییرات و مدیریت Automate وایت لیست سرور این است که در نهایت این فایل را ویرایش کرده و یک مرتبه دستور 
/vcl reload
را در کنسول پروکسی سرور جهت بازخوانی لیست بازیکنان اجرا کنیم

### نیازهای پروژه من
نیاز من همانطور که اشاره کردم این بود که در بازه های زمانی خاص یوزرنیم های معینی را در سرور وایت لیست کنم و موارد قبلی پاکسازی شوند اما در همین حین شماری staff در سرور وجود داشت که بایستی همواره در وایت لیست باقی میماندند بدین منظور من ابزار را بگونه ای نوشتم که دو فایل Permanet.txt و Temp.txt را در هر مرتبه اجرا مدنظر قرار دهد و یوزرنیم هارا از آنها خوانده و به فرمت مدنظر در فایل whitelist.json ذخیره سازی کند و این فایل دقیقا با همین نام و فرمت سمت سرور خوانده میشود به همین دلیل با دستور scp آنرا به سرور ماینکرفت منتقل میکند و با اولین اجرای دستور vcl reload وایت لیست طبق خواسته من تغییر میابد

همانطور که در ابزار send players اشاره کردم bottleneck این ابزار نیز میتواند روند جمع آوری و ذخیره یوزرنیم ها باشد که طبق توضیحات من آنها را از یک google sheat میخواندم که ابزار خوانش خودکار داده ها از sheet در دایرکتوری آن ابزار موجود است و در commit های آینده نیز به اینجا اضافه خواهد شد


اما رویکرد ویژه ای که برای راحتی بحث مدیریت یوزرنیم ها باتوجه به ساختار تیم و راحتی staff ها بنظرم آمد یکپارچه سازی ابزار با یک ربات تلگرامی بود

آن هم بدلیل اینکه همانطور که اشاره کردم تلگرام رایج ترین شبکه اجتماعی در کشور من است

در این دایرکتوری فارغ از ابزار اصلی، اسکریپت telegramintegrated.py یک ربات تلگرام را با دریافت توکن از شما مستقر میکند که یوزرنیم های Temp Whitelist را بصورت یک Message با فرمت Line Separated دریافت کرده و پس از ایجاد فایل whitelist.json در دایرکتوری خودش آنرا با scp به سرور ماینکرفت شما ارسال میکند که بدین منظور SSH Credentials سرور شما را نیز نیاز دارد

در نظر داشته باشید که این ابزار بر روی یک سرور ثانویه مستقر میشود و میزبانی تلگرام بات شما را بر عهده دارد آن هم به این دلیل بود که در پروژه من تصمیم نداشتم از سرور اصلی بعنوان میزبانی ربات استفاده کنم بدلایلی، پس سرور ثانویه ای برای این منظور استفاده کردم که با سرور اصلی بدین صورت ارتباط میگرفت

</div>

<div dir="rtl" align="right">

### پیش پردازش یوزرنیم های نادرست

ضمنا من در برنامه اصلی یکسری توابع پردازنده برای تمیز کردن یوزر های غلط از طریق یکسری رویکردها معمول مثلا حذف کارکتر های غلط مثل Whitespace Chars پیاده سازی کردم
(از آنجا که میدانیم یوزرنیم های ماینکرفت نمیتوانند کارکتر اسپیس داشته باشند)

با این حال انتظار میرود لیست یوزرنیم هایی که شما بر روی آن این ابزار را اجرا میکنید از قبل پیش پردازش شده باشند یا به اصطلاح "Pre-Processed Data" باشند

</div>