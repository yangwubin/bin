'''
1.有老王这个对象
2.枪对象
3.弹夹对象
4.一堆子弹
5.将子弹放入弹夹中
6.将弹夹放入枪中
7.有敌人
8.老王拿枪
9.打敌人
'''
class Person:
	def __init__(self,name):
		self.name=name
		self.gun=None
	#老王安装子弹
	def putBullToClip(self,clip,bullet):
		#将子弹保存到弹夹
		clip.baocunBull(bullet)
	def putClipToGun(self,clip,gun):
		gun.baocunClip(clip)		
	#拿枪方法
	def naqiang(self,gun):
		self.gun=gun
	def koubanji(self,diren):
		#扣扳机开火
		self.gun.fire(diren)
	def diaoxue(self,typeBull):
		if self.xue>0:
			self.xue-=typeBull	


class Gun:
	def __init__(self,name):
		self.name=name
		self.baocun1=None
	def baocunClip(self,clip):
		if not self.baocun1:
			self.baocun1=clip
	def fire(self,diren):
		return self.baocun1.jianshaozidan()


	def __str__(self):
		if self.baocun1:
			return "当前枪的信息为%s,当前有弹夹"%(self.name)


		else:
			return "当前枪的信息为%s,当前没有弹夹"	%(self.name)	


class Clip:
	def __init__(self,numMax):
		self.numMax=numMax
		self.baocun=[]
	def baocunBull(self,bullet):
		self.baocun.append(bullet)
	def __str__(self):
		return "当前弹夹的状态为%d/%d"%(len(self.baocun),self.numMax)	
	def jianshaozidan(self):
		if self.baocun:
			return self.baocun.pop()		#pop表示去除最后一个元素
		else:
			return None	


class Bullet:
	def __init__(self,typeBull):   #typeBull 杀伤力
		self.typeBull=typeBull
	def dazhong(self,diren):
		diren.diaoxue()	

def main():
	laowang=Person('老王')
	Qbz95=Gun('Qbz95')
	clip=Clip(20)
	bullet=Bullet(10)
	laowang.putBullToClip(clip,bullet)
	laowang.putClipToGun(clip,Qbz95)
	gebilaowang=Person("隔壁老王")
	laowang.naqiang(Qbz95)
	laowang.koubanji(gebilaowang)
main()	