const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  pwa: {
    name: 'Hoist',
    themeColor: '#f27059',
    msTileColor: '#343a40',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',

    // configure the workbox plugin
    // workboxPluginMode: 'InjectManifest',
    // workboxOptions: {
      // swSrc is required in InjectManifest mode.
      // swSrc: 'dev/sw.js',
      // ...other Workbox options...
    // }
  }
})
