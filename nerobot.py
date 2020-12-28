import discord
import datetime
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print(str(datetime.datetime.today()) + "\n----------\n봇 이름 : " + str(client.user) + "\n----------\n" + str(client.user) + "봇이 " +  str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 로그인 했습니다.")
#로그 채팅    await client.get_channel(792757695828197387).send("<@" + str(client.user.id) + ">봇이 " + str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 로그인 했습니다.\n\n`" + str(datetime.datetime.today()) + "`")
    messages = [f"노래 재생 기능 추가중 !!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(2)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    # /청소
    if message.content.startswith("=청소"):
        try:
            amount = message.content[4:]
            await message.channel.purge(limit = int(amount))
            embed = discord.Embed(color=0x819FF7)
            embed.add_field(name=str(client.user), value="메시지 " + str(amount) + "개가 청소되었습니다.", inline=True)
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            #CMD로그
            print("----------\n" + str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 명령어를 실행했습니다! ( " + str(datetime.datetime.today()) + " ) ( /청소 " + str(amount) + " )\n메시지 " + str(amount) + "개를 청소했습니다")
            print("----------\nid : " + str(message.author.id) + " | name,tag : " + str(message.author)  + "\nserver id : " + str(message.guild.id) + " | server name : " + str(message.guild) + "\nchannel id : " + str(message.channel.id) + " | channel name : " + str(message.channel) + "\nmessage id : " + str(message.id) + "\nLink : https://discordapp.com/channels/" + str(message.guild.id) + "/" + str(message.channel.id) + "/" + str(message.id) + "/")            
            #로그 채팅
            #embed = discord.Embed(color=0xc4a5df)
            #embed.add_field(name=str(client.user), value="----------\n메시지 " + str(amount) + "개가 청소되었습니다.\n" + "----------\n사용자 :" + str(message.author) + "\n사용시간 :"+ str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초\n" + "----------\nid : " + str(message.author.id) + " | name,tag : " + str(message.author)  + "\nserver id : " + str(message.guild.id) + " | server name : " + str(message.guild) + "\nchannel id : " + str(message.channel.id) + " | channel name : " + str(message.channel) + "\nmessage id : " + str(message.id) + "\n----------\nLink : https://discordapp.com/channels/" + str(message.guild.id) + "/" + str(message.channel.id) + "/" + str(message.id) + "/" + "\n----------", inline=True)
            #embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            #await client.get_channel(int(792757695828197387)).send(embed=embed)
        except ValueError:
            embed = discord.Embed(color=0x819FF7)
            embed.add_field(name=str(client.user), value="청소하실 메시지의 개수를 입력해 주세요", inline=True)
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
    # /테스트
    if message.content.startswith("=테스트"):
        embed = discord.Embed(color=0x819FF7)
        embed.add_field(name=str(client.user), value="테스트 123", inline=True)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        #CMD로그
        print("----------\n" + str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초에 명령어를 실행했습니다!")
        print("----------\nid : " + str(message.author.id) + " | name,tag : " + str(message.author)  + "\nserver id : " + str(message.guild.id) + " | server name : " + str(message.guild) + "\nchannel id : " + str(message.channel.id) + " | channel name : " + str(message.channel) + "\nmessage id : " + str(message.id) + "\nLink : https://discordapp.com/channels/" + str(message.guild.id) + "/" + str(message.channel.id) + "/" + str(message.id) + "/")            
        #로그 채팅
        #embed = discord.Embed(color=0xc4a5df)
        #embed.add_field(name=str(client.user), value="----------\n테스트 명령어를 실행했습니다!\n" + "----------\n사용자 :" + str(message.author) + "\n사용시간 :"+ str(datetime.datetime.today().year) + "년 " + str(datetime.datetime.today().month) + "월 " + str(datetime.datetime.today().day) + "일 " + str(datetime.datetime.today().hour) + "시 " + str(datetime.datetime.today().minute) + "분 " + str(datetime.datetime.today().second) + "초\n" + "----------\nid : " + str(message.author.id) + " | name,tag : " + str(message.author)  + "\nserver id : " + str(message.guild.id) + " | server name : " + str(message.guild) + "\nchannel id : " + str(message.channel.id) + " | channel name : " + str(message.channel) + "\nmessage id : " + str(message.id) + "\n----------\nLink : https://discordapp.com/channels/" + str(message.guild.id) + "/" + str(message.channel.id) + "/" + str(message.id) + "/" + "\n----------", inline=True)
        #embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        #await client.get_channel(int(792757695828197387)).send(embed=embed)
    
    if message.content.startswith("=도움말"):
        embed = discord.Embed(color=0x819FF7)
        embed.add_field(name=str(client.user), value="----------\n안녕하세요! 네로봇입니다.\n 네로봇의 기본 명령어는 = 입니다.\n----------\n명령어 음악관련\n=p 노래제목 - 노래제목의 노래는 틉니다.\n=s - 재생 중인 노래를 넘깁니다.\n=q - 현재 재생 준비중인 노래 목록을 띄웁니다.\n=j - 저를 통화방으로 소환시킵니다.\n=l - 저를 통화방에서 강퇴시킵니다. ㅠㅠ\n----------\n채팅 명령어\n=청소 갯수 - 갯수만큼의 채팅을 제가 쓱-싹 합니다.", inline=True)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
    if message.content.startswith("=l"):
        vc = self.voice_client_in(guild)
        if not vc:
            return

        if guild.id in self.players:
            self.players.pop(guild.id).kill()

        await vc.disconnect()

#@client.event
#async def on_member_join(member):
    #await client.get_channel(int(792647562644422676)).send("123")
#   await client.get_member("경고 받을시 개인디코로 알림이 옵니다!\n 갑자기 알림이 와도 놀라지 말아요! ㅎㅎ")
    #await client.get_channel(int(792647562644422676)).send("🖼️안녕하세요! {0.mention}님! ☕현치네카페☕에 오신걸 환영합니다\n 먼저 안내를 받아주세요!\n @안내원 을 맨션해주시면 안내해드리겠습니다.\n 오지않는다면 조금 기다려주세요🖼️")
# 접속메시지
    #channel = client.get_channel('792647562644422676"')
    #await member.send('방가방가\n $ 명령어를 통해 다양한 서비스를 제공받을 수 있으니 해보라구 !') #privit 한 메세지를 보내줌
    #await channel.send('안뇽')

    #server = member.server
    #fmt = 'Welcome {0.mention} to {1.name}!'
    #await client.send_message(server, fmt.format(member, server))

#@client.event
#async def on_member_join(member):
#    channel = client.get_channel('792647562644422676')
#    await member.send('경고 받을시 개인디코로 알림이 옵니다!\n 갑자기 알림이 와도 놀라지 말아요! ㅎㅎ')#privit 한 메세지를 디엠으로 보내줌
#    await channel.send('🖼️안녕하세요! @(member)님! ☕현치네카페☕에 오신걸 환영합니다\n 먼저 안내를 받아주세요!\n @안내원 을 맨션해주시면 안내해드리겠습니다.\n 오지않는다면 조금 기다려주세요🖼️')#privit 한 메세지를 서버에 보내줌
# 접속메시지

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
# 봇 토큰
