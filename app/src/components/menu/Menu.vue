<template>
    <div class="menu">
        <transition appear name="appear">
            <div class="left" v-show="$parent.isshow">
                <div class="item" v-for="(item, index) in items" :key="index">
                    <div class="img"  @click="goto(index)" :class="{now: $route.path === item.path}">
                        <svg-icon :iconClass="item.icon" className="icon"/>
                        <div class="tip">{{item.tip}}</div>
                    </div>
                </div>
            </div>
        </transition>
        <transition appear name="toleft">
            <div class="message" v-show="$parent.isshow">
                <div class="title">
                    <div class="tit">{{now.title}}</div>
                    <div class="desc">{{now.desc}}</div>
                    <slot></slot>
                </div>
                <div class="tools">
                    <div class="tool" data-str="返回首页">
                        <svg-icon iconClass="home" className="icon" @click.native="goHome"/>
                    </div>         
                    <div class="tool" data-str="后退">
                        <svg-icon iconClass="back" className="icon" @click.native="back"/>
                    </div>
                    <div class="tool" data-str="前进">
                        <svg-icon iconClass="forward" className="icon" @click.native="forward"/>
                    </div>
                </div>
                
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        name: 'Menu',
        data(){
            return {
                items: [
                    {
                        path: '/targetextraction',
                        tip: '目标提取',
                        icon: 'targetExtraction'
                    },
                    {
                        path: '/changedetection',
                        tip: '变化检测',
                        icon: 'changeDetection'
                    },
                    {
                        path: '/targetdetection',
                        tip: '目标检测',
                        icon: 'targetDetection'
                    },
                    {
                        path: '/classification',
                        tip: '地物分类',
                        icon: 'classification'
                    }
                ],
            }
        },
        computed: {
            now(){
                switch(this.$route.path) {
                    case '/targetextraction':
                        return {
                            title: '目标提取',
                            desc: '使用图像分割技术对卫星图像中指定对象完成分割,从而提取不同的图像特征'
                        }
                    case '/changedetection':
                        return {
                            title: '变化检测',
                            desc: '使用图像分割技术对同区域两个时期的卫星图像变化情况完成分析'
                        }
                    case '/targetdetection':
                        return {
                            title: '目标检测',
                            desc: '是一种基于目标几何和统计特征的图像分割。使用目标检测技术对卫星图像中指定对象完成检测'
                        }
                    case '/classification':
                        return {
                            title: '地物分类',
                            desc: '使用图像分割技术对卫星图像每个像素完成分类。在对遥感影像进行像素级内容解析，对遥感影像中感兴趣的类别进行提取和分类。'
                        }
                    default:
                        return {
                            title: '',
                            desc: ''
                        }
                }

            }
        },
        methods: {
            // 路由跳转
            goto(index){
                index += 1
                const {path} = this.$route
                switch(index){
                    case 1:
                        if (path !== '/targetextraction'){
                            this.$parent.isshow = false
                            const timer1 = setTimeout(() => {
                                this.$router.push({path: '/targetextraction'})
                                clearTimeout(timer1)
                            }, 800);
                        }
                        break
                    case 2:
                        if (path !== '/changedetection') {
                            this.$parent.isshow = false
                            const timer2 = setTimeout(() => {
                                this.$router.push({path: '/changedetection'})
                                clearTimeout(timer2)
                            }, 800);
                        }
                        break
                    case 3:
                        if (path !== '/targetdetection') {
                            this.$parent.isshow = false
                            const timer3 = setTimeout(() => {
                                this.$router.push({path: '/targetdetection'})
                                clearTimeout(timer3)
                            }, 800);
                        }
                        break
                    case 4:
                        if (path !== '/classification') {
                            this.$parent.isshow = false
                            const timer4 = setTimeout(() => {
                                this.$router.push({path: '/classification'})
                                clearTimeout(timer4)
                            }, 800);
                        }
                        break
                }
            },
            // 返回首页
            goHome(){
                this.$parent.isshow = false
                const timer = setTimeout(() => {
                    this.$router.push({path: '/home'})
                    clearTimeout(timer)
                }, 800);
            },
            // 前进
            forward(){
                this.$parent.isshow = false
                const timer = setTimeout(() => {
                    this.$router.forward()
                    clearTimeout(timer)
                }, 800);
            },
            // 后退
            back(){
                this.$parent.isshow = false
                const timer = setTimeout(() => {
                    this.$router.back()
                    clearTimeout(timer)
                }, 800);
            }

        }
    }
</script>

<style lang='less' scoped>
    .menu {
        width: 100%;
        height: 28%;
        display: flex;
    }
    .left {
        width: 180px;
        height: 100%;
    }
    .item {
        width: 200px;
        height: 25%;
        .now {
            color: var(--menu-now-font-color) !important;
            background-color: var(--menu-now-bg-color) !important;
        }
        .img {
            width: 50px;
            height: 42px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-top-right-radius: 21px;
            border-bottom-right-radius: 21px;
            background-color: var(--menu-bg-color);
            padding-right: 12px;
            cursor: pointer;
            transition: all .3s;
            color: var(--menu-font-color);
            &:hover {
                width: 125px;
            }
            &:hover .tip{
                display: block;
                color: inherit;
            }
            .icon {
                width: 35px !important;
                height: 35px !important;
                color: inherit;
            }
            .tip {
                overflow: hidden;
                display: none;
                flex: 1;
                text-align: center;
                font-size: 17px;
                line-height: 42px;
                height: 100%;
                color: transparent;              
            }
        }
    }

    .message {
        flex: 1;
        margin: 20px 55px 20px 0px;
        background-color: var(--menu-message-bg-color);
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        border: 1px solid var(--memu-border-color);
        .title {
            .tit {
                padding-top: 10px;
                padding-bottom: 10px;
                padding-left: 30px;
                font-weight: 600;
                font-size: 28px;
                color: var(--menu-message-title-color);
            }
            .desc {
                margin-left: 100px;
                font-size: 17px;
                position: relative;
                height: 20px;
                line-height: 20px;
                color: var(--menu-message-desc-color);
                &::before {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 10px;
                    height: 10px;
                    left: -17px;
                    top: 25%;
                    border-radius: 50%;
                    background-color: var(--menu-message-dian-color);
                }
            }
        }      
        .tools {
            width: 100%;
            height: 40px;
            position: absolute;
            bottom: 0px;
            left: 0;
            display: flex;
            justify-content: right; 
            align-items: top;
            .tool {
                width: 80px;
                height: 30px;
                display: flex;
                align-items: center; 
                justify-content: center;
                position: relative;
                background-color: var(--menu-tools-bg-color);
                border: 1px solid var(--memu-border-color);
                .icon {
                    width: 20px !important;
                    height: 20px !important;
                    color: var(--menu-tools-font-color);
                    cursor: pointer;
                    transition: all .5s;
                    &:hover {
                        transform: translateY(-3px);
                    }
                } 
                &:hover::before {
                    display: block;
                    position: absolute;
                    content: attr(data-str);
                    width: 70px;
                    top: -28px;
                    right: 0px;
                    font-size: 14px;
                    text-align: center;
                    color: var(--theme-select-text-color);
                    border-radius: 3px;
                    background-color: var(--theme-select-text-bg-color);
                }
                &:nth-child(1){
                    border-radius: 5px 0 0 5px;
                    border-right: none;
                }
                &:nth-child(3){
                    border-left: none;
                    margin-right: 20px;
                    border-radius: 0 5px 5px 0;
                }
            }
        }
    }


    @keyframes appear {
        0% {
            opacity: 0;
            transform: translateX(-100%);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }
    .appear-enter-active{
        animation: appear .8s;
    }
    .appear-leave-active{
        animation: appear .8s reverse;
    }

    
    .toleft-enter-active{
        animation: toleft .8s;
    }
    .toleft-leave-active{
        animation: toleft .8s reverse;
    }
</style>