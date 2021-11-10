import discord
import os



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("하구봇테스트")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content.startswith('안녕'):
        await message.channel.send('안녕하세요 하구봇입니다')

    if message.content.startswith('필쌀'):
        await message.channel.send('망해라')

    if message.content.startswith('재련'):
        await message.channel.send('파삭')

    if message.content == "명령어목록": # 안녕이라고해야만 나옴
        await message.channel.send('!하구 !호구 !하르 !메인쿤 !엑자일 !구구 !레몬 !조필쌀 ')

    if message.content.startswith('명령어'):
        await message.channel.send('찻집 부캐확인하기 : !하구')
        await message.channel.send('파티멤버 확인하기 : ?check날짜')
        await message.channel.send('예시 : ?check1109')

    if message.content.startswith('!하구'):
        embed = discord.Embed(title="HAx9",description="ha가 아홉개라서 하구님,귀여움^^", color=0x00aaaa)
        embed.add_field(name="김하구", value="하구님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★☆☆☆☆ 매우쉬움", inline=False)
        embed.add_field(name="⚔스카우터", value="슬기미안", inline=True)
        embed.add_field(name="🛡홀리나이트", value="독오른승모군", inline=True)
        embed.add_field(name="⚔스트라이커", value="슬해기", inline=True)
        embed.add_field(name="⚔블래스터", value="딕큼", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!하르'):
        embed = discord.Embed(title="하르",description="귀여운 하르하르, 산책그만해, 9시반이후 출몰", color=0x00aaaa)
        embed.add_field(name="하르", value="하르님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★☆☆☆☆ 매우쉬움", inline=False)
        embed.add_field(name="⚔호크아이", value="No에르", inline=True)
        embed.add_field(name="🛡바드", value="Ra에리", inline=True)
        embed.add_field(name="⚔스카우터", value="카즈하르", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!메인쿤'):
        embed = discord.Embed(title="입생로냥",description="매너있는 란제리 전문가, 길드장, 새벽반", color=0x00aaaa)
        embed.add_field(name="메인쿤", value="쿤님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★★★★★ 매우어려움", inline=False)
        embed.add_field(name="⚔건슬링어", value="리베스트라", inline=True)
        embed.add_field(name="🛡홀리나이트", value="입생로냥", inline=True)
        embed.add_field(name="⚔인파이터", value="인파속고독", inline=True)
        embed.add_field(name="⚔배틀마스터", value="라인힐데", inline=True)
        embed.add_field(name="⚔소서리스", value="프리베", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!엑자일'):
        embed = discord.Embed(title="Exile",description="비주류각인 전문, 우리들의 선생님, 부길드장, 새벽반", color=0x00aaaa)
        embed.add_field(name="엑자일", value="엑자님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★★★★☆ 어려움", inline=False)
        embed.add_field(name="⚔블레이드", value="르루주", inline=True)
        embed.add_field(name="⚔리퍼", value="말차젠", inline=True)
        embed.add_field(name="⚔버서커", value="라에스파다", inline=True)
        embed.add_field(name="⚔건슬링어", value="에스코페타라", inline=True)
        embed.add_field(name="⚔데빌헌터", value="케프카", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!조필쌀'):
        embed = discord.Embed(title="라인충",description="핑공(핑크공주), 카운터전문인력, 다요체의 창시자, 4차원이지만 괜찮아, 주말근무 평일밤접속", color=0x00aaaa)
        embed.add_field(name="조필쌀", value="필쌀님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★★★★☆  어려움", inline=False)
        embed.add_field(name="⚔워로드", value="등짝을보는자", inline=True)
        embed.add_field(name="⚔워로드", value="Esc키없어요", inline=True)
        embed.add_field(name="⚔블래스터", value="서버실감자에싹틈", inline=True)
        embed.add_field(name="⚔디트로이드", value="핑크공룡디붕", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!호구'):
        embed = discord.Embed(title="HOx9",description="ho가 아홉개라서 호구님, 채고미녀, 단골손님(카제섭)", color=0x00aaaa)
        embed.add_field(name="이호구", value="호구님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★★★★★ 매우어려움", inline=False)
        embed.add_field(name="🛡바드", value="낙지가비빔냉면", inline=True)
        embed.add_field(name="🛡바드", value="아보카도바나나스무디", inline=True)
        embed.add_field(name="⚔워로드", value="서윗트", inline=True)
        embed.add_field(name="⚔배틀마스터", value="목장소녀하이C", inline=True)
        embed.add_field(name="⚔스카우터", value="으하핳하핳하핳하핳하핳하", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!구구'):
        embed = discord.Embed(title="쿠크린",description="쿠그린구구링구구린", color=0x00aaaa)
        embed.add_field(name="구구링", value="구구님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★★★☆☆ 어렵지않음", inline=False)
        embed.add_field(name="⚔워로드", value="에들렌", inline=True)
        embed.add_field(name="⚔배틀마스터", value="엘네린", inline=True)
        embed.add_field(name="⚔소서리스", value="아누에", inline=True)
        embed.add_field(name="🛡홀리나이트", value="퀴테", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('!레몬'):
        embed = discord.Embed(title="Seraphim",description="레몬 소믈리에", color=0x00aaaa)
        embed.add_field(name="사라", value="사라님이라고 불러주세요", inline=False)
        embed.add_field(name="호감도작난이도", value="★★★★★ 매우어려움", inline=False)
        embed.add_field(name="🛡바드", value="신레몬", inline=True)
        embed.add_field(name="🛡홀리나이트", value="허니레몬브레드", inline=True)
        embed.add_field(name="⚔스카우터", value="매운레몬", inline=True)
        embed.add_field(name="⚔소서리스", value="아이스레몬홍차", inline=True)
        await message.channel.send(embed=embed)





access_token = os.environ['BOT_TOKEN']
client.run('access_token')
