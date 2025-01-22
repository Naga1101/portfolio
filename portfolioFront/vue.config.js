const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
<<<<<<< HEAD
  publicPath: process.env.NODE_ENV === 'production' ? '/portfolio/' : '/'
=======
  publicPath: '/'
>>>>>>> refs/remotes/origin/main
})
