# -*- coding:utf-8 -*-
from discord.ext import commands
import discord
import string
import os.path
import time
import os
import random
import sys
import pymysql
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

# @bot.command(pass_context=True, aliases=['help'])
# async def 도움말(ctx):
#     embed = discord.Embed(title = "제로봇 도움말", description='안녕하세요 제로봇 입니다.\n버그, 문의는 [제로봇 커뮤니티](https://discord.gg/BwK9t3c)로 알려주세요!')
#     embed.set_author(name="zerohwani#9367", url="http://www.zerohwani.com",icon_url="https://cdn.discordapp.com/avatars/283193429574418432/9905fb1f4fbdd4ea25800aea045bebce.png?size=256")
#     embed.add_field(name="기능", value="욕설 자동 감지(on/off)", inline=False)
#     embed.add_field(name="명령어", value="!필터설정 : 욕설을 감지할 언어를 설정 합니다.(여러개를 설정할 떄는 띄어쓰기로 구분합니다.)\n ex)!필터설정 욕설1 욕설2", inline=False)
#     embed.set_footer(text="zerohwani#9367", icon_url="https://cdn.discordapp.com/avatars/283193429574418432/1d6d86ac5bdd67555078321debc079dd.webp?size=256")
#     await ctx.send(embed=embed)

# con = pymysql.connect(host="zerohwani.com", user="zerohwani",
#                       password="cH914311", db='zerohwani', charset="utf8")
# cur = con.cursor()

# @bot.command(pass_context=True, aliases=['help'])
# async def 상점(ctx):
#     try:
#         add = ctx.message.content[4:]
#         add1 = add.split(' ')
#         if add1[0] == "":
#             await ctx.send("닉네임을 입력해주세요")
#         elif add1[1] == "":
#             await ctx.send("점수를 입력해주세요")
#         else:
#             if os.path.isfile('member.txt'):
#                 memberFile = open('member.txt', 'r', encoding='utf-8')
#                 memberGet = memberFile.readlines()
#                 for i in memberGet:
#                     list1 = i.split(' ')
#                 for i in list1:
#                     if i == add1[0]:
#                         sql = "update ddokddak1 set score=score + 1 where name='{}'".format(
#                             add1[0])
#                         cur.execute("set names utf8")
#                         cur.execute(sql)
#                         return await ctx.send(f'{add1[0]}님의 점수가 {add1[1]}점 올랐습니다')
#                 return await ctx.send(f'{add1[0]}님은 등록되지 않은 클랜원입니다.')

#     except IndexError:
#         await ctx.send('점수를 입력 해주세요')


@bot.command(pass_context=True)
async def 가입승인(ctx, member: discord.Member = None):
    role = discord.utils.get(ctx.guild.roles, name="승인")
    await member.add_roles(role)


# @bot.command(pass_context=True)
# async def 내정보(ctx):
#     sql = "select * from ddokddak1 where name = '단무지' "
#     cur.execute("set names utf8")
#     cur.execute(sql)
#     print(sql)
#     result = cur.fetchone()
#     await ctx.send(sql)
#     await ctx.send(result)


# @bot.command(pass_context=True)
# async def 클랜등록(ctx):
#     b_filter = ctx.message.content[6:]
#     ItemFile = open('member.txt', 'a', encoding='utf-8')
#     readFile = open('member.txt', 'r', encoding='utf-8')
#     l_filter = readFile.readline()
#     print(l_filter)
#     print(b_filter)
#     if(len([i for i in l_filter if i != ' ']) == 0):
#         ItemFile.write('{}'.format(b_filter))
#     else:
#         ItemFile.write(' {}'.format(b_filter))
#     await ctx.send('{'+b_filter+'}'+'추가 성공')

# extentions = ['cogs.filter']
# if __name__ == '__main__':
#     for ext in extentions:
#         bot.load_extension(ext)
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
