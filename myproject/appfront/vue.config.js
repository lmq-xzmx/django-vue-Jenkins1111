const path = require('path')

function resolve (dir) {
  return path.join(__dirname, dir)
}

module.exports = {
    publicPath: './',
	//publicPath: process.env.NODE_ENV === 'production' 
	//	? '/sts/' 
	//	: '/',
	outputDir:'dist', //Type: string 
	assetsDir:'static', 
	indexPath:'index.html',
	//indexPath指定生成的 index.html 的输出路径 (相对于 outputDir)。也可以是一个绝对路径。
	//lintOnSave:false,//是否开启eslint保存检测 ,它的有效值为 true || false || 'error'
	
	filenameHashing:true,
	pages: {
	    
		bookapi: {
	      // page 的入口
	      entry: 'src/package/bookapi/bookapi.js',
	      // 模板来源
	      template: 'public/bookapi.html',
	      // 在 dist/bookapi.html 的输出
	      filename: 'bookapi.html',
	      // 当使用 title 选项时，
	      // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
	      title: 'bookapi的app',
	      // 在这个页面中包含的块，默认情况下会包含
	      // 提取出来的通用 chunk 和 vendor chunk。
	      chunks: ['chunk-vendors', 'chunk-common', 'bookapi']
	    },
		index: {
		  entry: 'src/package/testapi/main.js',
		  template: 'public/index.html',
		  filename: 'index.html',
		  title: 'testapi的app',
		  chunks: ['chunk-vendors', 'chunk-common', 'index']
		},
		echartsmap: {
		  entry: 'src/package/echartsmap/echartsmap.js',
		  template: 'public/echartsmap.html',
		  filename: 'echartsmap.html',
		  title: 'testapi的app',
		  chunks: ['chunk-vendors', 'chunk-common', 'echartsmap']
		},
		wechat: {
		  entry: 'src/package/wechat/wechat.js',
		  template: 'public/wechat.html',
		  filename: 'wechat.html',
		  title: 'wechat的app',
		  chunks: ['chunk-vendors', 'chunk-common', 'wechat']
		},
	
	    // 当使用只有入口的字符串格式时，
	    // 模板会被推导为 `public/subpage.html`
	    // 并且如果找不到的话，就回退到 `public/index.html`。
	    // 输出文件名会被推导为 `subpage.html`。
	    //subpage: 'src/subpage/main.js',
		//这个可以用来设置子入口
	  },
	lintOnSave: 'default',
	
	runtimeCompiler:false,//是否使用包含运行时编译器的 Vue 构建版本。
	//设置为 true 后你就可以在 Vue 组件中使用 template 选项了，但是这会让你的应用额外增加 10kb 左右。
	
	transpileDependencies:[],
	//默认情况下 babel-loader 会忽略所有 node_modules 中的文件。
	//如果你想要通过 Babel 显式转译一个依赖，可以在这个选项中列出来。
	
	productionSourceMap:true,//如果你不需要生产环境的 source map，可以将其设置为 false 以加速生产环境构建
	
	
	
	devServer: {
		
		//index:"echartsmap.html",
		index:"wechat.html",
		//index:"bookapi.html",
		//index:"index.html",
		//host: "localhost",
		open: true ,
		//open: "Safari" ,
	    // 前端请求的链接
	    host: '127.0.0.1',
	    // 前端请求的端口
	    port: 8080,
	    // 代理
	    //proxy: {
	    //  '/': {
	    //    target: 'http://127.0.0.1:8099',
	    //    changeOrigin: true,
	    //    pathRewrite: {
	    //      '^/': '/'
	    //    }
	    //  }
	    //}
	  },
	chainWebpack: (config) => {
	    const alias = config.resolve.alias
	      alias.set('@', resolve('src'))
	      .set('@components', resolve('src/components'))
		  .set('@assets', resolve('src/assets'))
		  .set('@enty', resolve('src/enty'))
		  .set('@filters', resolve('src/filters'))
		  .set('@router', resolve('src/router'))
	  },

}