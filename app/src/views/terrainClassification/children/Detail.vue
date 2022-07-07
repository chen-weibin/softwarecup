<template>
    <div class="detaill">
        <div class="top">
            <div class="logolg">
                <img src="../../../assets/理工.png" alt="" class="lg">
            </div>
            <div class="title">
                |&nbsp;&nbsp;地物分类
            </div>
            <div class="returnbef">
                <span @click="returnHome">返回上一级</span>
            </div>
            <div class="returnhome">
                <span @click="returnMain">返回主页</span>
            </div>      
        </div>
        <div class="bottom">
            <div class="left">
                <div class="tit">上传示例</div>
                <div class="con">
                    <div class="item" v-for="(item, index) in showData" :key="index" :class="current === index ? 'current' : ''" @click="changeCurrent(index)">
                        <div class="image">
                            <img :src="item.resimg1" alt="">
                        </div>
                        <div class="bot"></div>
                    </div>
                </div>
            </div>
            <div class="center">
                <div class="image" ref="show">
                    <img :src="showData.length ? showData[current].resimg2 : ''" alt="" ref="img">
                    <div class="tools">
                        <svg-icon iconClass="fd" className="icon" @click.native="maxImage"/>
                        <svg-icon iconClass="sx" className="icon" @click.native="minImage"/>
                    </div>
                </div>
            </div>
            <div class="right">
                <div class="con">
                    <div class="item">
                        <div class="one head">土地类型</div>
                        <div class="two head">百分比</div>
                        <div class="three head">颜色</div>
                    </div>
                    <div class="item">
                        <div class="one">林地</div>
                        <div class="two">{{showData.length ? (showData[current].lingdi.ishave ? showData[current].lingdi.person  + '%': '未识别') : ''}}</div>
                        <div class="three">
                            <div class="lindi"></div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="one">耕地</div>
                        <div class="two">{{showData.length ? (showData[current].gendi.ishave ? showData[current].gendi.person + '%': '未识别') : ''}}</div>
                        <div class="three">
                            <div class="gengdi"></div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="one">建筑</div>
                        <div class="two">{{showData.length ? (showData[current].jianzhu.ishave ? showData[current].jianzhu.person + '%' : '未识别') : ''}}</div>
                        <div class="three">
                            <div class="jianzu"></div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="one">其他</div>
                        <div class="two">{{showData.length ? (showData[current].qita.ishave ? showData[current].qita.person + '%' : '未识别') : ''}}</div>
                        <div class="three">
                            <div class="qita"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {TerrainClassificationExample} from '@/api'
    export default {
        name: 'Detail',
        props: ['img', 'resimg', 'resdata'],
        data() {
            return {
                current: 0,
                showData: []
            }
        },
        methods: {
            returnHome(){
                this.$parent.isDetail = false
            },
            returnMain() {
                this.$parent.isDetail = false
                this.$router.push({path: '/home'})
            },
            setImageLocation(left, top) {
                const width = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("width"))
                const height = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("height"))
                if (left < 0 && left + width >= 708) {
                    this.$refs.img.style.left = left + 'px'
                    if (top < 0 && top + height >= 708) {
                        this.$refs.img.style.top = top + 'px'
                    }
                }
            },
            setImageSize(width, height) {       
                this.$refs.img.style.width = width + 'px'
                this.$refs.img.style.height = height + 'px'
            },
            maxImage() {
                const width = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("width"))
                const height = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("height"))
                this.setImageSize(width + 80, height + 80)
                const left = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("left"))
                const top = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("top"))
                this.$refs.img.style.left = left - 40 + 'px'
                this.$refs.img.style.top = top - 40 + 'px'
            },
            minImage() {
                console.log('now')
               
                const width = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("width"))
                if (width - 80 <= 708) {
                    this.$refs.img.style.width = '708px'
                    this.$refs.img.style.height = '708px'
                    this.$refs.img.style.left = '0px'
                    this.$refs.img.style.top = '0px'
                } else {
                    const left = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("left"))
                    const top = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("top"))
                    const right = width - Math.abs(left) - 708
                    const bottom = width - Math.abs(top) - 708
                    if (Math.abs(left) >= 40 && right >= 40) {
                        this.$refs.img.style.left = left + 40 + 'px'
                    } else if (Math.abs(left) < 40) {
                        this.$refs.img.style.left = '0px'
                    } else {
                        this.$refs.img.style.left = left + 80 - right + 'px'
                    }

                    if (Math.abs(top) >= 40 && bottom >= 40) {
                        this.$refs.img.style.top = top + 40 + 'px'
                    } else if (Math.abs(top) < 40) {
                        this.$refs.img.style.top = '0px'
                    } else {
                        this.$refs.img.style.top = top + 80 - bottom + 'px'
                    }
                    this.setImageSize(width - 80, width - 80)

                }  
            },
            changeCurrent(index) {
                this.current = index
            }
        },
        mounted() {
            TerrainClassificationExample().then((res) => {
                const {data} = res.data
                for (let i = 0; i < data.length; i++) {
                    this.showData.push(data[i])          
                }
            }, error => {})

            this.$refs.show.style.background = 0
            this.$refs.show.onmousedown = (e) => {
                const x = e.clientX + document.body.scrollLeft - this.$refs.show.offsetLeft
                const y = e.clientY + document.body.scrollTop - this.$refs.show.offsetTop - 50
                const left = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("left"))
                const top = parseInt(window.getComputedStyle(this.$refs.img, null).getPropertyValue("top"))
                this.$refs.show.onmousemove = (e)=>{
                    const newX = e.clientX + document.body.scrollLeft - this.$refs.show.offsetLeft
                    const newY = e.clientY + document.body.scrollTop - this.$refs.show.offsetTop - 50
                    const distanceX = newX - x
                    const distanceY = newY - y
                    this.setImageLocation(left + distanceX, top + distanceY)  
                }
                this.$refs.show.onmouseleave = ()=>{
                    this.$refs.show.onmousemove = null
                }
                this.$refs.show.onmouseup = ()=>{
                    this.$refs.show.onmousemove = null
                }
                
            }
        },
        watch: {
            resimg: {
                immediate: true,
                handler(){
                    if (this.resimg) {
                        const len = this.showData.length
                        const {lingdi, gendi, jianzhu, qita} = this.resdata
                        if (len === 5) {      
                            this.showData.unshift({
                                resimg1: this.img,
                                resimg2: this.resimg,
                                lingdi,
                                gendi,
                                jianzhu,
                                qita
                            })
                        } else {
                            this.showData[0] = {
                                resimg1: this.img,
                                resimg2: this.resimg,
                                lingdi,
                                gendi,
                                jianzhu,
                                qita
                            }
                        }
                    }
                }
            }
        },
    }
</script>

<style lang='less' scoped>
    .detaill {
        width: 100%;
        height: 100vh;
        position: absolute;
        left: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 9999;
        .bottom {
            width: 100%;
            height: calc(100% - 50px);
            position: relative;
        }
    }

    .top {
        width: 100%;
        height: 50px;
        background-color: #000000;
        .logolg {
            float: left;
            margin-left: 40px;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            .lg {
                width: 35px;
                height: 35px;
            }
        }
        .title {
            float: left;
            width: 125px;
            height: 50px;
            line-height: 50px;
            color: white;
            font-weight: 700;
            font-size: 21px;
            text-align: center;
        }
        .returnbef{
            float: right;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            span {
                height: 28px;
                width: 80px;
                font-weight: 700;
                color: white;
                line-height: 28px;
                text-align: center;
                margin-right: 30px;
                cursor: default;
            }
        }
        .returnhome{
            float: right;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            span {
                height: 28px;
                width: 80px;
                font-weight: 700;
                color: white;
                line-height: 28px;
                text-align: center;
                margin-right: 15px;
                cursor: default;
            }
        }
    }

    .left {
        position: absolute;
        left: 0;
        top: 0;
        height: calc(100% - 50px);
        width: 400px;
        display: flex;
        justify-content: center;
        align-items: center;
        .tit {
            width: 100%;
            height: 40px;
            position: absolute;
            top: 12px;
            left: 0;
            color: white;
            line-height: 40px;
            text-align: center;
            font-size: 20px;
            font-weight: 700;
        }
        .con {
            width: 230px;
            height: 550px;
            overflow-y: auto;
            padding: 5px 15px;
            &::-webkit-scrollbar {
                display: none;
            }
            .item {
                width: 200px;
                height: 180px;
                margin-bottom: 70px;
                position: relative;
                &::before {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 20px;
                    height: 20px;
                    left: -3.5px;
                    top: -3.5px;
                    border-top: 3.5px solid rgb(0, 247, 255);
                    border-left: 3.5px solid rgb(0, 247, 255);
                }
                &::after {
                    display: block;
                    position: absolute;
                    content: '';
                    width: 20px;
                    height: 20px;
                    right: -3.5px;
                    top: -3.5px;
                    border-top: 3.5px solid rgb(0, 247, 255);
                    border-right: 3.5px solid rgb(0, 247, 255);
                }
                .time {
                    width: 100%;
                    height: 15px;
                    color: white;
                    line-height: 15px;
                    text-align: center;
                    overflow: hidden;
                    font-size: 14px;
                }
                .image {
                    width: 100%;
                    height: calc(100% - 15px);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    img {
                        width: 155px;
                        height: 155px;
                    }
                }
                .bot {
                    &::before {
                        display: block;
                        position: absolute;
                        content: '';
                        width: 20px;
                        height: 20px;
                        left: -3.5px;
                        bottom: -3.5px;
                        border-bottom: 3.5px solid rgb(0, 247, 255);
                        border-left: 3.5px solid rgb(0, 247, 255);
                    }
                    &::after {
                        display: block;
                        position: absolute;
                        content: '';
                        width: 20px;
                        height: 20px;
                        right: -3.5px;
                        bottom: -3.5px;
                        border-bottom: 3.5px solid rgb(0, 247, 255);
                        border-right: 3.5px solid rgb(0, 247, 255);
                    }
                }
            }
            .current {
                box-shadow: 3px 3px 6px 2px #7ccccf;
            }
        }
    }

    .center {
        margin: 0 auto;
        width: 708px;
        height: calc(100% - 50px);
        -webkit-user-drag: none;
        .image {
            width: 708px;
            height: 708px;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            -webkit-user-drag: none;
            img {
                position: absolute;
                width: 708px;
                height: 708px;
                left: 0;
                top: 0;
                -webkit-user-drag: none;
            }
            .tools {
                position: absolute;
                top: 20px;
                right: 30px;
                width: 95px;
                height: 40px;
                padding: 3px 7px;
                background: rgba(0, 0, 0, 0.5);
                display: flex;
                border-radius: 5px;
                justify-content: space-between;
                align-items: center;
                transition: all .5s;
                -webkit-user-drag: none;
                .icon {
                    width: 30px !important;
                    height: 30px !important;
                    color: rgb(3, 247, 255);
                    &:hover {
                        transform: translateY(-2px);
                    }
                }
            }
        }
    }

    .right {
        position: absolute;
        top: 0;
        right: 0;
        width: 400px;
        height: calc(100% - 50px);
        display: flex;
        justify-content: center;
        align-items: center;
        .con {
            width: 300px;
            height: 310px;
            padding: 20px 15px;         
            border-radius: 8px;
            color: #abd4fd;
            background-color: #0F3A65;
            .item {
                width: 100%;
                height: 35px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 17px;
                .one {
                    width: 100px;
                    height: 35px;
                    line-height: 35px;
                    padding-left: 5px;
                }
                .two {
                    width: 50px;
                    flex: 1;
                    height: 35px;
                    line-height: 35px;
                    padding-left: 5px;
                }
                .three {
                    width: 70px;
                    height: 35px;
                    line-height: 35px;
                    padding-left: 5px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    .lindi {
                        height: 20px;
                        width: 38px;
                        background: rgb(60, 0, 255);
                    }
                    .gengdi {
                        height: 20px;
                        width: 38px;
                        background: rgb(255, 222, 0);
                    }
                    .jianzu {
                        height: 20px;
                        width: 38px;
                        background: rgb(30, 255, 142);
                    }
                    .qita {
                        height: 20px;
                        width: 38px;
                        background: rgb(255, 0, 0);
                    }
                }
                .head {
                    font-size: 17.5px;
                    color: #ffffff;
                }
            }
        }
    }

    // .a {
    //     background: rgb(0, 115, 225);
    //     background: rgb(83, 255, 98);
    //     background: rgb(255, 189, 57);
    //     background: rgb(0, 255, 234);
    // }
</style>