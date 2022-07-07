<template>
    <div class="header">
        <div class="tools">
            <div class="themetool">
                <theme />
            </div>
            <div class="screenmax" :data-str="str">
                <svg-icon iconClass="fullScreen" className="icon" v-if="!isFullScreen" @click.native="maxScreen"/>
                <svg-icon iconClass="cancelScreen" className="icon" v-else @click.native="cancelScreen"/>
            </div>    
            <div class="fj">
                <a href="https://www.paddlepaddle.org.cn/" class="link" target="_blank" data-str="访问飞桨官网">飞桨官网</a>
            </div>
            <div class="user">
                <div class="tx">
                    <img src="../../assets/yk.svg" alt="">
                    <div class="detail">
                        <div class="yonghu">
                            <div>
                                <img src="../../assets/yk.svg" alt="">
                            </div>
                            <h4>{{user}}</h4>   
                        </div> 
                        <hr>  
                        <div class="item">
                            <ul>
                                <li>
                                    <svg-icon iconClass="account" className="bef"/>
                                    <span>当前账号</span>
                                    <div>{{username}}</div>
                                </li>
                                <li>
                                    <svg-icon iconClass="time" className="bef"/>
                                    <span>加入时间</span>
                                    <div>{{jointime}}</div>
                                </li>
                                <li>
                                    <svg-icon iconClass="cishu" className="bef"/>
                                    <span>使用次数</span>
                                    <div>{{times}}次</div>
                                </li>
                                <li @click="gotoLogin">
                                    <svg-icon iconClass="qiehuan" className="bef"/>
                                    <span>切换账号</span>
                                    <svg-icon iconClass="right" className="right"/>
                                </li>
                                <li @click="gotoLogin">
                                    <svg-icon iconClass="tuichu" className="bef"/>
                                    <span>退出登录</span>
                                    <svg-icon iconClass="right" className="right"/>
                                </li>
                            </ul>
                        </div>                  
                    </div>
                </div>
            </div>
            <div class="xmut">
                <img src="../../assets/理工.png" alt="">
            </div>
            <div class="js">
                <div class="jsti">
                    团队介绍
                    <div class="desc">
                        <div class="row">
                            <span class="be">学校名称：</span>&nbsp;
                            <span>厦门理工学院</span>
                        </div>
                        <div class="row">
                            <span class="be">队伍名称：</span>&nbsp;
                            <span>我们连头发都卷</span>
                        </div>
                        <div class="row">
                            <span class="be">指导老师：</span>&nbsp;
                            <span>陈&nbsp;&nbsp;思</span>
                        </div>
                        <div class="row">
                            <span class="be">&nbsp;队&nbsp;&nbsp;&nbsp;&nbsp;长&nbsp;&nbsp;:</span>&nbsp;&nbsp;&nbsp;
                            <span>施&nbsp;&nbsp;斌</span>
                        </div>
                        <div class="row">
                            <span class="be">团队成员：</span>&nbsp;
                            <span>张天乐、苏均杰、</span>
                        </div>         
                        <div class="row">
                            <span class="be">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>&nbsp;
                            <span>陈伟宾</span>
                        </div>                      
                    </div>
                </div>
            </div>
            
        </div>
        <div class="title">
            遥感图像解译
        </div>  
    </div>
</template>

<script>
    import Theme from '@/components/theme/Theme.vue'

    import {requestFullScreen, exitFullScreen} from '@/utils/window'
    import {getUser} from '@/api'
    import {getCookie} from "@/utils/cookie"
    export default {
        name: 'Header',
        components: { Theme },
        data(){
            return {
                isFullScreen: false, // 是否全屏
                str: '全屏', //提示信息,
                user: '',
                username: '',
                jointime: '',
                times: 0,
                
            }
        },
        methods: {
            maxScreen(){
                requestFullScreen()
                this.isFullScreen = true
                this.str = '退出全屏'
            },
            cancelScreen(){
                exitFullScreen()
                this.isFullScreen = false
                this.str = '全屏'
            },
            gotoLogin() {
                this.$router.push({path: '/login'})
            }
        },
        mounted(){
            const cookie = getCookie('xmut')
            if (cookie === '999999') {
                this.user = '游客'
                this.username = '游客登录'
                this.jointime = '游客登录'
                this.times = '0'
            } else{
                if (cookie) {
                    getUser({token: cookie}).then((response) => {
                        const {user, username, jointime, times} = response.data
                        this.user = user
                        this.username = username
                        const time = jointime.split(' ')
                        this.jointime = `${time[3]}-${time[2]}-${time[1]}`
                        this.times = times
                    }, error => {})
                } else {
                    this.$router.push({path: '/login'})
                }     
            }
        }
    }
</script>

<style lang='less' scoped>
    .header {
        width: 100%;
        height: 12%;
        background-color: var(--header-bg-color);
        .tools {
            height: 35px;
            .screenmax {
                float: right;
                height: 35px;
                height: 35px;
                margin: 0 3px;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                .icon {
                    width: 29px !important;
                    height: 29px !important;
                    color: var(--max-min-screen);
                    cursor: pointer;
                    transition: all .5s;
                    &:hover {
                        transform: translateY(-2px);
                    }
                    
                }
                &:hover::before {
                    display: block;
                    position: absolute;
                    content: attr(data-str);
                    width: 70px;
                    top: 33px;
                    right: -20px;
                    font-size: 14px;
                    text-align: center;
                    color: var(--theme-select-text-color);
                    border-radius: 3px;
                    background-color: var(--theme-select-text-bg-color);
                }
                
            }
            .themetool {
                width: 40px;
                height: 35px;
                float: right;
                margin: 0 3px;
                margin-right: 10px;      
            }
            .fj {
                float: right;
                height: 35px;
                width: 75px;
                margin: 0 3px;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                .link {
                    text-decoration: none;
                    color: var(--max-min-screen);
                    font-size: 16px;
                    transition: all .5s;
                    &:hover {
                        transform: translateY(-2px);
                    }
                    &:hover::before {
                        display: block;
                        position: absolute;
                        content: attr(data-str);
                        width: 95px;
                        top: 33px;
                        right: -15px;
                        font-size: 14px;
                        text-align: center;
                        color: var(--theme-select-text-color);
                        border-radius: 3px;
                        background-color: var(--theme-select-text-bg-color);
                    }
                }
            }
            .user {
                float: right;
                height: 35px;
                width: 35px;
                margin: 0 0px;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2px;
                .tx {  
                    width: 100%;
                    height: 100%;
                    border-radius: 50%;  
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: all .5s;
                    position: relative;
                    cursor: pointer;
                    background-color: #fff;
                    z-index: 50;
                    &:hover {
                        transform: translateY(-2px);
                    } 
                    &:hover .detail {
                        display: block;
                    }  
                    .detail {
                        display: none;
                        position: absolute;
                        content: '';
                        width: 280px;
                        height: 400px;
                        top: 35px;
                        left: -150px;
                        border-radius: 6px;
                        border: 1px solid var(--user-bg-border);
                        color: var(--main-font-color);
                        background-color: var(--user-bg);
                        .yonghu {
                            width: 100%;
                            padding-top: 20px;
                            div {
                                width: 55px;
                                height: 55px;
                                overflow: hidden;
                                border-radius: 50%;
                                margin: 0 auto;
                                background-color: var(--user-touxiang);
                                img {
                                    width: 100%;
                                    height: 100%;
                                }
                            }
                            h4 {
                                margin-top: 6px;
                                margin-bottom: 8px;
                                color: var(--main-font-color);
                                text-align: center;
                            }
                        }
                        .item {
                            width: 100%;
                            margin-top: 10px;
                            ul {
                                list-style: none;
                                color: var(--user-list-font);
                                padding: 0 10px;
                                li {
                                    width: 100%;
                                    height: 50px;
                                    border-radius: 6px;
                                    display: flex;
                                    justify-content: left;
                                    align-items: center;
                                    padding: 0 8px;
                                    span {
                                        margin-left: 8px;
                                        font-size: 15px;
                                    }
                                    .bef {
                                        width: 27px !important;
                                        height: 27px !important;
                                        color: inherit;
                                    }
                                    .right {
                                        margin-left: 120px;
                                        width: 22px !important;
                                        height: 22px !important;
                                        color: inherit;
                                    }
                                    div {
                                        margin-left: 15px;
                                        font-size: 14px;
                                    }
                                    &:hover {
                                        background-color: var(--user-show);
                                    }
                                }
                            }
                        }
                        hr {
                            border-radius: 50%;
                            width: 88%;
                            margin: 0 auto;
                            background-color: #dbdbdb;
                        }
                    }
                    img {
                        width: 100%;
                        height: 100%;
                    }
                }
            }
            .xmut {
                float: left;
                position: relative;
                img {
                    position: absolute;
                    left: 10px;
                    width: 88px;
                    // animation: 280pxrotate 10s linear infinite;
                }
            }
            .js {
                float: right;
                height: 35px;
                width: 75px;
                margin: 0 3px;
                display: flex;
                align-items: center;
                justify-content: center;
                .jsti {
                    color: var(--max-min-screen);
                    font-size: 16px;
                    transition: all .5s;
                    cursor: pointer;
                    position: relative;
                    z-index: 1000;
                    &:hover {          
                        transform: translateY(-2px);
                    }
                    &:hover .desc {
                        display: block;
                    }
                    .desc {
                        display: none;
                        position: absolute;
                        top: 26px;
                        left: -100px;
                        width: 260px;
                        height: 300px;
                        overflow: hidden;
                        border-radius: 6px;
                        border: 1px solid var(--user-bg-border);
                        color: var(--main-font-color);
                        background-color: var(--user-bg);
                        padding: 20px 15px;
                        .row {
                            width: 100%;
                            height: 40px;
                            border-radius: 6px;
                            line-height: 40px;
                            padding-left: 4px;
                            &:hover {
                                background-color: var(--user-show);
                            }
                            .be {
                                font-weight: 700;
                            }
                        }
                    }
                }
            }
        }

        .title {
            width: 100%;
            height: calc(100% - 35px);
            text-align: left;
            color: var(--title-color);
            font-size: 40px;
            padding-left: 110px; //25
        }
        
    }

    // @keyframes rotate {
    //     0% {
    //         transform: rotate(0);
    //     }
    //     100% {
    //         transform: rotate(360deg);
    //     }
    // }
</style>