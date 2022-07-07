const path = require('path')

module.exports = {
    assetsDir: 'static',
    lintOnSave: process.env.NOOD_ENV !== 'production',

    chainWebpack(config) {
        config.module
        .rule('svg')
        .exclude.add(path.resolve(__dirname, 'src/icons'))
        .end()
        config.module
        .rule('icons')
        .test(/\.svg$/)
        .include.add(path.resolve(__dirname, 'src/icons'))
        .end()
        .use('svg-sprite-loader')
        .loader('svg-sprite-loader')
        .options({
            symbolId: 'icon-[name]'
        })
        .end()
    }
}