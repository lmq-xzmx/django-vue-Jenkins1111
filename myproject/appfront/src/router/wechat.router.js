import Vue from 'vue'
import Router from 'vue-router'

import wechat  from '@/components/wechat/wechat'
import dialogue  from '@/components/wechat/dialogue'
import addfriend  from '@/components/contact/addfriend'
import dialogueinfo  from '@/components/wechat/dialogueinfo'
import dialoguedetail  from '@/components/wechat/dialoguedetail'
import contact  from '@/components/contact/contact'
import details  from '@/components/contact/details'
import mobilecontacts  from '@/components/contact/mobilecontacts'
import officialaccounts  from '@/components/contact/officialaccounts'
import grouplist  from '@/components/contact/grouplist'
import newfriends  from '@/components/contact/newfriends'
import tags  from '@/components/contact/tags'
import explore  from '@/components/explore/explore'
import moments  from '@/components/explore/moments'
import self  from '@/components/self/self'
import album  from '@/components/common/album'
import settings  from '@/components/self/settings'
import security  from '@/components/self/settings/security'
import notice  from '@/components/self/settings/notice'
import privacy  from '@/components/self/settings/privacy'
import common  from '@/components/self/settings/common'
import profile  from '@/components/common/profile'
import myqrcode  from '@/components/self/myqrcode'
import settings2  from '@/components/settings/settings'
import common2  from '@/components/settings/common/common'
import language  from '@/components/settings/common/language'

Vue.use(Router)

const routes = [
    {
        path: '/',
        name: "微信",
		component: wechat
        //component: resolve => require(["@/components/wechat/wechat.vue"], resolve)
    }, {
        path: '/wechat/dialogue',
        name: "",
            components: {
				"default": wechat,
				"subPage":dialogue
            //"default": resolve => require(["@/components/wechat/wechat.vue"], resolve),
            //"subPage": resolve => require(["@/components/wechat/dialogue.vue"], resolve)
        }
    },
    {
        path: '/wehchat/addfriend',
        name: "",
        components: {
			"default": wechat,
			"subPage": addfriend
            //"default": resolve => require(["@/components/wechat/wechat.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/addfriend.vue"], resolve)
        }
    },
    {
        path: '/wechat/dialogue/dialogueinfo',
        name: "",
        components: {
			"subPage":dialogueinfo
            //"subPage": resolve => require(["@/components/wechat/dialogueinfo.vue"], resolve)
        }
    },
    {
        path: '/wechat/dialogue/dialoguedetail',
        name: "",
        components: {
			"subPage":dialoguedetail
            //"subPage": resolve => require(["@/components/wechat/dialoguedetail.vue"], resolve)
        }
    },
    {
        path: '/contact',
        name: "通讯录",
        component: contact
		//component: resolve => require(["@/components/contact/contact.vue"], resolve)
    },
    {
        path: '/contact/addfriend',
        name: "",
        components: {
			"default": contact,
			"subPage":addfriend
            //"default": resolve => require(["@/components/contact/contact.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/addfriend.vue"], resolve)
        }
    },
    {
        path: '/contact/details',
        name: "",
        components: {
			"default": contact,
			"subPage": details
            //"default": resolve => require(["@/components/contact/contact.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/details.vue"], resolve)
        }
    },
    {
        path: '/contact/new-friends/mobilecontacts',
        name: "通讯录朋友",
        components: {
			"subPage":mobilecontacts
            //"subPage": resolve => require(["@/components/contact/mobilecontacts.vue"], resolve)
        }
    },
    {
        path: '/contact/officialaccounts',
        name: "",
        components: {
			"default": contact,
			"subPage": officialaccounts
            //"default": resolve => require(["@/components/contact/contact.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/officialaccounts.vue"], resolve)
        }
    },
    {
        path: '/contact/grouplist',
        name: "",
        components: {
			"default":contact,
			"subPage":grouplist
            //"default": resolve => require(["@/components/contact/contact.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/grouplist.vue"], resolve)
        }
    },
    {
        path: '/contact/newfriends',
        name: "",
        components: {
			"default":contact,
			"subPage":newfriends
            //"default": resolve => require(["@/components/contact/contact.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/newfriends.vue"], resolve)
        }
    }, {
        path: '/contact/tags',
        name: "新的朋友",
        components: {
			"default":contact,
			"subPage":tags
            //"default": resolve => require(["@/components/contact/contact.vue"], resolve),
            //"subPage": resolve => require(["@/components/contact/tags.vue"], resolve)
        }
    }, {
        path: '/explore',
        name: "发现",
        component:explore
		//component: resolve => require(["@/components/explore/explore.vue"], resolve)
    }, {
        path: '/explore/moments',
        name: "朋友圈",
        components: {
            "default": explore,
			"subPage":moments
			//"default": resolve => require(["@/components/explore/explore.vue"], resolve),
            //"subPage": resolve => require(["@/components/explore/moments.vue"], resolve)
        }
    }, {
        path: '/self',
        name: "我",
        //component: resolve => require(["@/components/self/self.vue"], resolve)
		component:self
    }, {
        path: '/self/album',
        components: { 
			"default":self,
			"subPage": album
			//"default": resolve => require(["@/components/self/self.vue"], resolve), 
			//"subPage": resolve => require(["@/components/common/album.vue"], resolve) 
			}
    },
    {
        path: '/self/settings',
        components: { 
			"default":self,
			"subPage":settings
			//"default": resolve => require(["@/components/self/self.vue"], resolve), 
			//"subPage": resolve => require(["@/components/self/settings.vue"], resolve) 
			}
    }, {
        path: '/self/settings/security',
        components: { 
			"subPage":security
			//"subPage": resolve => require(["@/components/self/settings/security.vue"], resolve) 
			}
    },
    {
        path: '/self/settings/notice',
        components: { 
			"subPage":notice
			//"subPage": resolve => require(["@/components/self/settings/notice.vue"], resolve) 
			}
    },
    {
        path: '/self/settings/privacy',
        components: { 
			"subPage":privacy
			//"subPage": resolve => require(["@/components/self/settings/privacy.vue"], resolve) 
			}
    }, {
        path: '/self/settings/common',
        components: { 
			"subPage": common
			//"subPage": resolve => require(["@/components/self/settings/common.vue"], resolve) 
			}
    },
    {
        path: '/self/profile',
        components: { 
			"default":self,
			"subPage": profile
			//"default": resolve => require(["@/components/self/self.vue"], resolve), 
			//"subPage": resolve => require(["@/components/common/profile.vue"], resolve) 
			}
    }, {
        path: '/self/profile/myqrcode',
        components: { 
			"subPage":myqrcode
			//"subPage": resolve => require(["@/components/self/myqrcode.vue"], resolve) 
			}
    }, {
        path: '/self/settings',
        components: { 
			//"subPage":settings
			"subPage":settings2
			//"subPage": resolve => require(["@/components/settings/settings.vue"], resolve) 
			}
    },
    {
        path: '/self/settings/common',
        components: {
			//"subPage":common
			"subPage":common2
            //"subPage": resolve => require(["@/components/settings/common/common.vue"], resolve)
        }
    },
    {
        path: '/self/settings/common/language',
        components: {
            "subPage":language
			//"subPage": resolve => require(["@/components/settings/common/language.vue"], resolve)
        }
    }
    
]
export default new Router({
    //base: "/vue-wechat/",
    routes,
    // scrollBehavior(to, from, savedPosition) {
    //     if (savedPosition) {
    //         return savedPosition
    //     } else {
    //         return { x: 0, y: 0 }
    //     }
    // }

})
