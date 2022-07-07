<template>
    <div class="login">
        <div class="main">
            <div class="title">遥感图像解译</div>
            <div class="choice">
                <div class="left cho" :class="{now: current}" @click="choice(1)">账号登录</div>
                <div class="right cho" :class="{now: !current}" @click="choice(2)">注册账号</div>
            </div>
            <div class="zhlogin" v-show="current">
                <div class="message">
                    <div class="account">
                        <svg-icon iconClass="account" className="icon"></svg-icon>
                        <input class="input" type="text" placeholder="账号" v-model="username">
                    </div>
                    <div class="password">
                        <svg-icon iconClass="password" className="icon"></svg-icon>
                        <input class="input" type="password" placeholder="密码" v-model="password">
                    </div>
                    <div class="yzm">
                        <svg-icon iconClass="yzm" className="icon"></svg-icon>
                        <input type="text" class="input" placeholder="验证码" v-model="verificationCode">
                        <img :src="img" alt="" @click="reCreate">
                    </div>
                </div>
                <div class="tip">
                    <div class="left">
                        <input type="checkbox" class="check" :checked="checked" @change="changeCheck">
                        <span>7天内免登陆</span>    
                    </div> 
                    <div class="right">忘记密码？</div>
                </div>
                <div class="but">
                    <button class="lg" @click="login">登录</button>
                </div>
                <div class="line">
                    <div class="lin1"></div>
                    <div class="text">其他登录方式</div>
                    <div class="lin2"></div>
                </div>
                <div class="qt">
                    <div class="yk" @click="ykLogin">
                        <img src="../../assets/yk.svg" alt="">
                    </div>
                </div>
            </div>
            <div class="zclogin" v-show="!current">
                <div class="bef" v-if="!isapply">
                    <div class="form">
                        <div class="user">
                            <svg-icon iconClass="user" className="icon"></svg-icon>
                            <input class="input" type="text" placeholder="用户名" v-model="zcUser">
                        </div>
                        <div class="password">
                            <svg-icon iconClass="password" className="icon"></svg-icon>
                            <input class="input" type="password" placeholder="密码" v-model="zcPassword">
                        </div>
                        <div class="yzpassword">
                            <svg-icon iconClass="yzpassword" className="icon"></svg-icon>
                            <input class="input" type="password" placeholder="确认密码" v-model="zcPasswordAgain">
                        </div>
                        <div class="email">
                            <svg-icon iconClass="email" className="icon"></svg-icon>
                            <input class="input" type="text" placeholder="邮箱" v-model="zcEmail">
                        </div>
                    </div>
                    <div class="but">
                        <button class="lg" @click="apply">注册</button>
                    </div>
                </div>
                <div class="after" v-if="isapply">
                    <div class="one">恭喜注册成功</div>
                    <div class="tw">
                        您当前的用户信息为：<br/>
                        用户名：{{zcUser}}<br/>
                        账号：{{zcUsername}}<br/>
                        更多信息请访问：<a href="https://www.paddlepaddle.org.cn/" target="_blank">百度飞浆平台</a>
                    </div>
                    <div class="thr">
                        <button class="imm" @click="applyLogin">立即登录</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { generateCaptcha, CaptchaMode } from "@tuzhanai/captcha";
    import {login, registered} from '@/api'
    import {setCookie} from '@/utils/cookie'

    export default {
        name: 'Login',
        data() {
            return {
                current: true,  //是登陆还是注册
                img: null,   // 验证码
                text: '',   // 验证码内容
                checked: false, // 是否选择7天免登陆
                username: '',
                password: '',
                verificationCode: '', //输入的验证码
                zcUser: '',
                zcPassword: '',
                zcPasswordAgain: '',
                zcEmail: '',
                zcUsername: '',
                zcToken: '',
                isapply: false,
            }
        },
        methods: {
            choice(index) {
                switch(index) {
                    case 1:
                        this.current = true
                        break
                    case 2:
                        this.current = false
                        break
                }
            },
            createYZM() {
                const { text, data } = generateCaptcha(CaptchaMode.Easy)  //CaptchaMode.Medium
                let binary = '';
                for (let i = 0; i < data.byteLength; i++) {
                    binary += String.fromCharCode(data[i])
                }
                const img = 'data:image/png;base64,'+ window.btoa(binary)
                return {text, img}
            },
            changeCheck(event){
                this.checked = event.target.checked
            },
            // 判断验证码是否正确
            verify(){
                return this.text === this.verificationCode.toLocaleLowerCase()
            },
            login(){
                const {username, password, verificationCode} = this
                let temp = true
                if (verificationCode === '') {
                    this.$toast.warning('请输入验证码')
                    temp = false
                }
                if (password === ''){
                    this.$toast.warning('请输入密码')
                    temp = false
                }
                if (username === '') {
                    this.$toast.warning('请输入账号')
                    temp = false
                }    
                if (username === '' && password === '' && verificationCode === '') {
                    this.$toast.warning('请输入登录信息')
                    temp = false
                }
                if (temp) {
                    if (this.verify()) {
                        login(this.username, this.password).then((response) => {
                            const {token} = response.data
                            if (token !== -1) {
                                if (this.checked) {
                                    setCookie('xmut', token, 60 * 60 * 24 * 7)
                                } else {
                                    setCookie('xmut', token)
                                }
                                this.$router.push({path: '/home'})  
                            } else {
                                this.$toast.warning('账号或密码错误')
                                this.reCreate()
                            }
                        }, error => {})
                    } else {
                        this.$toast.warning('验证码错误')
                        this.verificationCode = ''
                        const {img, text} = this.createYZM()
                        this.img = img  
                        this.text = text.toLocaleLowerCase()
                    }
                }
            },
            reCreate(){
                const {img, text} = this.createYZM()
                this.img = img  
                this.text = text.toLocaleLowerCase()
            },
            ykLogin() {
                setCookie('xmut', '999999')
                this.$router.push({path: '/home'})
            },
            // 注册
            apply(){
                const {zcUser, zcPassword, zcPasswordAgain, zcEmail} = this
                let temp = true
                if (zcEmail === ''){
                    this.$toast.warning('请输入邮箱')
                    temp = false
                }
                if (zcPasswordAgain === '') {
                    this.$toast.warning('请确认密码')
                    temp = false
                }
                if (zcPassword === '') {
                    this.$toast.warning('请设置密码')
                    temp = false
                }
                if (zcUser === '') {
                    this.$toast.warning('请输入用户名')
                    temp = false
                }
                if (temp) {
                    const re = /\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$/i
                    if (!re.test(zcEmail)) {
                        if (zcPasswordAgain === zcPassword) {
                            registered(this.zcUser, this.zcPassword, this.zcEmail).then((response) => {
                                const {username, token} = response.data
                                this.zcUsername = username
                                this.zcToken = token
                                this.isapply = true
                                setCookie('xmut', token)
                            }, error => {})
                        } else {
                            this.$toast.warning('两次输入的密码不一致')
                            this.zcPasswordAgain = ''
                        }      
                    } else {
                        this.$toast.warning('输入的邮箱格式错误')
                    }
                }
            },
            applyLogin(){
                setCookie('xmut', this.zcToken)
                this.$router.push({path: '/home'})
            }
        },
        mounted() {
            const {img, text} = this.createYZM()
            this.img = img  
            this.text = text.toLocaleLowerCase()
        }

    }
</script>

<style lang='less' scoped>
    .login {
        width: 350px;
        height: 440px;
        border-radius: 8px;
        padding: 13px 20px;
        background-color: rgba(255, 255, 255, .15);
        box-shadow: 0 0 8px 1px rgb(165, 165, 165);
    }
    .main {
        position: relative;
        width: 100%;
        height: 100%;
        .title {
            width: 100%;
            height: 45px;
            line-height: 45px;
            font-size: 30px;
            text-align: center;
            font-weight: 500;
            color: rgba(13, 227, 255, 0.8);
            letter-spacing:3px;
        }
        .choice {
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            margin-top: 3px;
            margin-bottom: 10px;
            height: 35px;
            .cho {
                width: 120px;
                height: 100%;
                color: white;
                text-align: center;
                font-size: 20px;
                line-height: 35px;
                position: relative;
                cursor: default;
                font-weight: 700;
            }
            .now::before {
                position: absolute;
                content: '';
                display: block;
                width: 84px;
                left: calc((100% - 84px) / 2);
                height: 3px;
                bottom: -2px;
                border-radius: 1.5px;
                background-color: rgba(135, 255, 253, 0.8);
            }
            .left {
                // background: red;
            }
            .right {
                
            }
        }
    }
    .zhlogin {
        width: 100%;
        height: calc(100% - 93px);
        overflow: hidden;
        .message {
            margin-top: 17px;
            width: 100%;
            height: 150px;
            padding-top: 9px;
            .account,
            .password {
                display: flex;
                justify-content: center;
                width: 100%;
                height: 37px;
                margin-bottom: 9px;
                .icon {
                    width: 28px;
                    height: 100%;
                    border-bottom: 2px solid white;
                    padding-right: 3px;
                    color: white;
                }
                .input {
                    border: none;
                    outline: none;
                    color: white;
                    font-size: 18px;
                    width: 215px;
                    background: transparent;
                    border-bottom: 2px solid white;
                    &::-webkit-input-placeholder {
                        color: #b9b9b9;
                        padding-left: 5px;
                        font-size: 14px;
                    }
                    &:focus {
                        padding-left: 5px;
                    }
                
                }
            }
            .yzm {
                width: 100%;
                height: 37px;
                margin-bottom: 9px;
                display: flex;
                justify-content: center;
                .icon {
                    width: 28px;
                    height: 100%;
                    border-bottom: 2px solid white;
                    padding-right: 3px;
                    color: white;
                }
                .input {
                    border: none;
                    outline: none;
                    color: white;
                    font-size: 18px;
                    width: 65px;
                    background: transparent;
                    border-bottom: 2px solid white;
                    &::-webkit-input-placeholder {
                        color: #b9b9b9;
                        padding-left: 5px;
                        font-size: 14px;
                    }
                    &:focus {
                        padding-left: 5px;
                    }
                
                }
                img {
                    margin-left: 80px;
                    margin-right: 2px;
                    height: 100%;
                }
            }
        }
        .tip {
            width: 100%;
            height: 20px;
            display: flex;
            padding:0 27px 0 33px;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: white;
            .left {
                padding-left: 3px;
                height: 100%;
                display: flex;
                line-height: 100%;
                align-content: center;
                justify-content: center;
                span {
                    height: 100%;
                    line-height: 20px;
                    padding-left: 3px;
                }
                .check {
                    height: 100%;
                }
            }
            .right {
                height: 100%;
                cursor: pointer;
            }
        }
        .but {
            width: 100%;
            height: 55px;
            display: flex;
            justify-content: center;
            align-items: center;
            .lg {
                width: 150px;
                height: 32px;
                border: none;
                border-radius: 5px;
                color: white;
                line-height: 32px;
                font-size: 16px;
                cursor: pointer;
                background-color: rgba(13, 227, 255, 0.8);
                &:hover {
                    box-shadow: 0 0 5px 1px #aeaeae;
                }
            }

        }
        .line {
            width: 100%;
            height: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            .lin1 {
                flex: 1;
                height: 1px;
                margin-left: 25px;
                margin-right: 3px;
                background-color: #fff;
            }
            .lin2 {
                flex: 1;
                height: 1px;
                margin-left: 3px;
                margin-right: 25px;
                background-color: #fff;
            }
            .text {
                color: white;
                font-size: 12px;
            }
        }
        .qt {
            width: 100%;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            .yk {
                width: 42px;
                height: 42px;
                border-radius: 50%;
                overflow: hidden;
                background-color: #fff;
                transition: all .5s;
                position: relative;
                img {
                    width: 100%;
                    height: 100%;
                }
                &:hover {
                    transform: translateY(-2px);
                }
            }
        }
    }
    .zclogin {
        width: 100%;
        overflow: hidden;
        height: calc(100% - 93px);
        .bef {
            width: 100%;
            height: 100%;
            .form {
                margin-top: 15px;
                width: 100%;
                height: 200px;
                .user,
                .password,
                .yzpassword,
                .email 
                {
                    display: flex;
                    justify-content: center;
                    width: 100%;
                    height: 37px;
                    margin-bottom: 9px;
                    .icon {
                        width: 28px;
                        height: 100%;
                        border-bottom: 2px solid white;
                        padding-right: 3px;
                        color: white;
                    }
                    .input {
                        border: none;
                        outline: none;
                        color: white;
                        font-size: 18px;
                        width: 215px;
                        background: transparent;
                        border-bottom: 2px solid white;
                        &::-webkit-input-placeholder {
                            color: #b9b9b9;
                            padding-left: 5px;
                            font-size: 14px;
                        }
                        &:focus {
                            padding-left: 5px;
                        }
                    
                    }
                }
            }
            .but {
                width: 100%;
                height: 50px;
                display: flex;
                justify-content: center;
                align-items: center;
                .lg {
                    width: 150px;
                    height: 32px;
                    border: none;
                    border-radius: 5px;
                    color: white;
                    line-height: 32px;
                    font-size: 16px;
                    cursor: pointer;
                    background-color: rgba(13, 227, 255, 0.8);
                    &:hover {
                        box-shadow: 0 0 5px 1px #aeaeae;
                    }
                }

            }
        }
        .after {
            width: 100%;
            height: 100%;
            .one {
                margin-top: 30px;
                width: 100%;
                height: 40px;
                color: rgb(26, 255, 228);
                line-height: 40px;
                font-size: 18px;
                padding-left: 8px;
            }
            .tw {
                width: 100%;
                height: 100px;
                margin-top: 10px;
                color: white;
                line-height: 20px;
                font-size: 16px;
                padding-left: 10px;
                a {
                    text-decoration: none;
                    color: rgb(51, 251, 228);
                }
            }
            .thr {
                margin-top: 32px;
                width: 100%;
                height: 70px;
                display: flex;
                justify-content: center;
                align-items: center;
                
                .imm {
                    width: 150px;
                    height: 32px;
                    border: none;
                    border-radius: 5px;
                    color: rgb(255, 255, 255);
                    line-height: 32px;
                    font-size: 16px;
                    cursor: pointer;
                    background-color: rgba(52, 243, 220, 0.8);
                    &:hover {
                        box-shadow: 0 0 5px 1px #aeaeae;
                    }
                }
            }

        }
    }
</style>