import random

seal_map = [
    {'img':'https://images.unsplash.com/photo-1493579706121-60161eb06eeb?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
     'description':'海豹回頭看著你'},{
         'img':'https://plus.unsplash.com/premium_photo-1667602674008-3f9654a9c2ee?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
         'description':'海豹抬頭看著你'},{
             'img':'https://images.unsplash.com/photo-1618075254460-429d47b887c7?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'海豹使出香蕉式'
         },
         {
             'img':'https://images.unsplash.com/photo-1533084417605-e538a510d50a?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'海豹聽到你的叫喚浮出水面'
         },{
             'img':'https://plus.unsplash.com/premium_photo-1666363528954-51382581c51a?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'你踩到海豹的尾巴，他慘叫了很大一聲'
         },{
             'img':'https://images.unsplash.com/photo-1557657043-23eec69b89c9?q=80&w=1746&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'海豹正在曬太陽，有點懶得理你'
         },{
             'img':'https://images.unsplash.com/photo-1618075254478-850bc1729c17?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'海豹被你的叫喚嚇到，大吃一驚'
         },{
             'img':'https://images.unsplash.com/photo-1559157693-c34156e0f8c3?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'海豹聽到你的叫喚，笑咪咪地邀你一起來躺躺'
         },{
             'img':'https://images.unsplash.com/photo-1587738972117-c12f8389f1d4?q=80&w=1752&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
             'description':'海豹聽到你的聲音，笑咪咪地對你揮揮他的短胖手'
         },{'img':'https://images.unsplash.com/photo-1572880393162-0518ac760495?q=80&w=1548&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'description':'海豹聽到你的聲音回頭，今天竟然有另一個海豹朋友來拜訪！'},{
                'img':'https://plus.unsplash.com/premium_photo-1667667846151-0553cc62157a?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'description':'海豹嘔噁了一聲，他正在和同伴們一起發懶'
            },{
                'img':'https://images.unsplash.com/photo-1470290488513-d7815dab2988?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'description':'海豹今天不知為何趴在草地上，看起來在思索著什麼'
            },{
                'img':'https://plus.unsplash.com/premium_photo-1661881453885-67cffaca4633?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'description':'海豹被你嚇到，跳回水里回家了'
            },{
                'img':'https://images.unsplash.com/photo-1713124209705-738f32bd8074?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'description':'海豹看到了你，邀你一起下水玩玩，在你猝不及防之際把你硬拖下水'
            },{'img':'https://images.unsplash.com/photo-1591731936001-6c726654d509?q=80&w=1752&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
               'description':'海豹正在做香蕉式，他邀起一起來學學他，看他多麽像根香蕉'}
     
]
def get_random_seal():
    return random.choice(seal_map)