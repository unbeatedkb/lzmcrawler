# coding: utf-8


html = '''
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.lianjia.com/hz/chengjiao/" >
<meta name="mobile-agent" content="format=html5;url=https://m.lianjia.com/hz/chengjiao/"><script>
ljConf = {
    city_id: '330100',
    city_abbr: 'hz',
    city_name: '杭州',
    channel: 'chengjiao',
    page: 'chengjiao_index',
    pageConfig: {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"},
    feroot: '//s1.ljcdn.com/feroot/',
    ucid:'',
    cdn:'1',
};
</script>

<title>杭州二手房网签|成交查询(杭州链家网)</title>
<meta name="description" content="杭州链家网发布杭州网签二手房成交信息,提供房源网签总价及面积均价和同户型成交记录,信息精准详细,方便您对倾向购买的杭州房源进行参考,查询杭州网签二手房信息,就到杭州链家网." />
<meta name="keywords" content="杭州二手房成交，杭州二手房,杭州二手房网签,杭州二手房走势,杭州二手房成交行情" />
<link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><link rel="stylesheet" href="http://s1.ljcdn.com/feroot/pc/asset/common.css?_v=20170504205919">
<link rel="stylesheet" href="http://s1.ljcdn.com/feroot/pc/asset/ershoufang/dealList/index.css?_v=20170504205919">
<!--[if lt IE 9]><script type="text/javascript" src="http://s1.ljcdn.com/feroot/dep/common-require/html5.js?_v=20170504205919"></script><![endif]-->
<script>
function RESIZEIMG(b,k,l,m){var c=b.parentNode;var d=parseInt(c.offsetWidth)||k;var e=parseInt(c.offsetHeight)||l;var f=d/e;var g=b.naturalWidth||b.width;var h=b.naturalHeight||b.height;var i=g/h;var j="width";if(f<i){j="height";try{b.style["left"]="-"+parseInt(Math.abs((d-(g*e/h))/2))+"px"}catch(e){}}else if(m){try{b.style["top"]="-"+parseInt(Math.abs((e-(h*d/g))/2))+"px"}catch(e){}};b.style[j]="100%";};
</script>
<script>
var _czc = _czc || [];
_czc.push(["_setAccount", "1254525948"]);
</script>

<script type="text/javascript">
var _smq = _smq || [];
_smq.push(['_setAccount', '41331c2', new Date()]);
_smq.push(['_setDomainName', 'lianjia.com']);
_smq.push(['pageview']);
(function() {
var sm = document.createElement('script'); sm.type = 'text/javascript'; sm.async = true;
sm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'cdnmaster.com/sitemaster/collect.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sm, s);
})();
</script>
</head><body><script>
__STAT_LJ_CONF = {
    params: {
        ljweb_group: ['SEARCH','BIGDATA_PC'],
        ljweb_id: '',
        ljweb_mod: '',
        ljweb_bl: '',
        ljweb_el: '',
        ljweb_sl: '',
        ljweb_index: '',
        ljweb_value: '',
        ljweb_url: '',
        ljweb_ljref: (document.cookie.match(/(?:^| )ljref=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_sample: (document.cookie.match(/(?:^| )sample_traffic_test=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_ref: document.referrer,
        ljweb_cid: '330100',
        ljweb_channel: 'chengjiao',
        ljweb_page: 'chengjiao_index',
        ljweb_source: '',
        ljweb_stat_id: ''
    }
};



var UT = {
    send: function() {

    }
};
var LjUserTrack = {
    log: [],
    initInterval: false,
    intervalLog: function() {
        setTimeout(function() {
            if(window.$ULOG && $ULOG.send) {
                for(var i = 0, l = LjUserTrack.log.length; i < l; i++) {
                    LjUserTrack.__send(LjUserTrack.log[i]);
                }

                for(var m = 0, n = LjUserTrack.logIds.length; m < n; m++) {
                    LjUserTrack.__sendId(LjUserTrack.logIds[m]);
                }
            } else {
                LjUserTrack.intervalLog();
            }
        }, 16.7);
    },
    _start_time: +new Date,
    __send: function(data) {
        var evt_id = data.evt_id || '10043';
        if('evt_id' in data) {
            delete data.evt_id;
        }

        $ULOG.send(evt_id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href,
            "action": data
        });
    },
    logIds: [],
    __sendId: function(id) {
        id && $ULOG.send(id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href
        });
    },
    sendId: function(id) {
        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__sendId(id);
        } else {
            LjUserTrack.logIds.push(id);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }
    },
    send: function(data, el, config) {

        var utConf = __STAT_LJ_CONF;
        var params = config || utConf.params,
            win = window,
            j;

        data.groupIndex = data.ljweb_group || 0;

        if (params) {
            for (var d in params) {
                if(params[d] !== j && data[d] === j) {
                    data[d] = params[d];
                }
            }
        }

        if(el) {
            this.checkClick(el, data);
        }

        data.ljweb_group = params['ljweb_group'][data.groupIndex || 0];

        delete data.groupIndex;

        if(data.typ) {
            data.ljweb_bl = (data.ljweb_bl || '') + '_' + data.typ;
            delete data.typ;
        }

        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__send(data);
        } else {
            LjUserTrack.log.push(data);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }

    },
    checkClick: function(el, data) {

        var TAG_LINK = 'A';
        var href = '';
        var elParent = null;

        href = (el.tagName.toUpperCase() === TAG_LINK ? el.getAttribute("href", 2) : '');
        if(!href && (elParent = el.parentNode) && elParent.nodeType === 1) {
            href = (elParent.tagName.toUpperCase() === TAG_LINK ? elParent.getAttribute("href", 2) : '');
        }

        if(href) {
            data.ljweb_url = href;
        } else {
            data.ljweb_url = data.ljweb_url
                  || el.getAttribute("data-log_url")
                  || (elParent=el.parentNode||el).getAttribute("data-log_url")
                  || (
                        (elParent=elParent.parentNode||elParent)
                     && (elParent.nodeType === 1)
                     && elParent.getAttribute("data-log_url")
                     )
                  || "";
        }

        this.attr(el, data);

    },
    path: function() {

    },
    attr: function(el, data) {
        var modId     = el.getAttribute("log-mod");
        var blAttr    = el.getAttribute("data-bl");
        var elAttr    = el.getAttribute("data-el");
        var slAttr    = el.getAttribute("data-sl");
        var InAttr    = el.getAttribute("data-log_index");
        var valAttr   = el.getAttribute("data-log_value");
        var idAttr    = el.getAttribute("data-log_id");
        var groupAttr = el.getAttribute("data-log_group");
        var sourceAttr = el.getAttribute("data-log_source");
        var statIdAttr = el.getAttribute("data-log_statId");
        var evtId     = el.getAttribute("data-log_evtid");

        data.ljweb_bl    = data.ljweb_bl || blAttr || '';
        data.ljweb_el    = data.ljweb_el || elAttr || '';
        data.ljweb_sl    = data.ljweb_sl || slAttr || '';
        data.ljweb_index = data.ljweb_index || InAttr || '';
        data.ljweb_value = data.ljweb_value || valAttr || '';
        data.ljweb_id    = data.ljweb_id || idAttr || '';
        data.ljweb_source    = data.ljweb_source || sourceAttr || '';
        data.ljweb_stat_id    = data.ljweb_stat_id || statIdAttr || 0;
        data.groupIndex  = data.groupIndex || groupAttr || 0;
        data.evt_id      = data.evt_id || evtId || '';

        if (!modId) {
            if (el.parentNode && el.parentNode.nodeType === 1 && el.parentNode.tagName.toUpperCase() !== 'BODY') {
                this.attr(el.parentNode, data);
            }
        } else {
            data.ljweb_mod = modId;
        }
    }
};

;;(function() {
    var isW3c = !!document.addEventListener;

    LjUserTrack.send({
        ljweb_mod: 'pv',
        ljweb_group: 1
    });

    /*window[isW3c ? 'addEventListener' : 'attachEvent'](
        (isW3c ? '': 'on') + 'beforeunload',
        function(e) {
            var _end_time = +new Date;
            UT.send({type: 'show', subtype: 'stay', time: (_end_time-UT._start_time)/1000});
        },
        false);*/
})();





</script>
<div class="banner"><div class="container"><ul class="channelList"><li><a href="//www.lianjia.com/">首页</a></li><li  class="selected"><a href="http://hz.lianjia.com/ershoufang/" >二手房</a></li><li  class=""><a href="http://hz.fang.lianjia.com/" >新房</a></li><li  class=""><a href="http://hz.lianjia.com/zufang/" >租房</a></li><li  rel="nofollow"  class=""><a href="http://you.lianjia.com/" >旅居地产</a></li><li  class=""><a href="http://us.lianjia.com/" >海外</a></li><li  class=""><a href="http://hz.lianjia.com/xiaoqu/" >小区</a></li><li  class=""><a href="http://hz.lianjia.com/jingjiren/" >经纪人</a></li><li  class=""><a href="http://hz.lianjia.com/wenda/" >指南</a><div class="childList"><a href="http://hz.lianjia.com/wenda/" >问答</a><a href="http://news.lianjia.com/hz/baike/" >百科</a></div></li><li  class=""><a href="http://hz.lianjia.com/yezhu/" target="_blank">卖房</a></li></ul><div class="banner-right"><div class="login" id="userInfoContainer"><i></i><a href="https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fhz.lianjia.com%2Fchengjiao%2F" id="loginBtn">登录</a>/<a href="https://passport.lianjia.com/register/resources/lianjia/register.html?service=http%3A%2F%2Fhz.lianjia.com%2Fchengjiao%2F" rel="nofollow">注册</a></div><div class="phone"><i></i><span>热线电话1010-9666</span></div></div></div></div>


<script type="text/template" id="userInfoTpl">
  <i></i>
  <%if(isAgent){%>
    <a id="userNameContainer" href="<%=$.env.fixedUrl('//agent.lianjia.com/')%>"><%=username%></a>
  <%}else{%>
    <a id="userNameContainer" href="<%=$.env.fixedUrl('//user.lianjia.com/')%>" rel="nofollow"><%=username%></a>
  <%}%>
  <span id="tipContainer"></span>
  &nbsp;&nbsp;<a href="<%=logoutUrl%>">退出</a>
  <span id="pushNewsListContainer"></span>
</script>
<script type="text/template" id="pushNewsListTpl">
  <div class="pushNewsList">
    <%for(var i in group_by_type){%>
      <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
        <a href="<%=pushMsgMap[i].url%>"><%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%></a>
      <%}%>
    <%}%>
  </div>
</script>
<div class="header"><div class="menu"><div class="menuLeft"><a href="/ershoufang" class="logo"></a><ul class="typeList"><li ><a href="/ershoufang/"  title="杭州在售二手房" >在售</a></li><li class="selected"><a href="/chengjiao/"  title="杭州成交二手房" >成交</a></li><li ><a href="/xiaoqu/"  title="杭州小区二手房" >小区</a></li><li ><a href="/ditu/"  title="杭州地图找房二手房" target="_blank">地图找房</a></li></ul></div><div class="app"><a href="//www.lianjia.com/client/" target="_blank"><i></i>下载链家APP</a></div></div><div class="search"><div class="input" log-mod="search"><form id="searchForm" action='/ershoufang/rs'><input type="text" id="searchInput" value="" autocomplete="off"><div class="inputRightPart"><div class="save" id="savedSearchMsg"><span id="savedSearchCount">0</span>条已保存搜索<span id="savedSearchArrow" class="downArrow"></span></div><button type='submit' class="searchButton" data-bl="search" data-el="search">&nbsp;<i></i>&nbsp;</button></div></form><div class="searchMsg" id="searchMsgContainer"></div></div></div></div>


<script type="text/template" id="hotSearchTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">热门搜索</span>
  </div>
  <ul data-bl="sug" data-el="history">
    <%for(var i =0; i < list.length; i++){%>
    <li>
      <a role="addHistory" href="<%=list[i].url%>" data-log_index="<%=i+1%>" data-log_value="<%=list[i].string%>" class="sug--search_item">
        <span class="msgListTitle" role="historyKey"><%=list[i].string%></span>
      </a>
    </li>
    <%}%>
  </ul>
</script>
<script type="text/template" id="searchHistoryTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">搜索历史</span>
    <div class="searchMsgTitleRightPart">
      <a href="#" id="clearSearchHistory" class="manage">清除历史记录</a>
    </div>
  </div>
  <ul data-bl="sug" data-el="history">
  <%for(var i = 0; i < list.length; i++){%>
    <li>
      <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=$.encodeHTML(list[i].name)%>" class="sug--search_item">
        <span class="msgListTitle" role="historyKey"><%=$.encodeHTML(list[i].name)%></span>
        <%if(list[i].newCount) {%>
          <span class="msgListAdd"><%=list[i].newCount%>套新增房源</span>
        <%}%>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="searchSuggestionTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">你可能在找</span>
  </div>
  <ul data-bl="sug" data-el="sug">
  <%for(var i = 0;i < list.length;i++){%>
    <li>
      <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=list[i].title%>">
        <span class="msgListTitle">
          <span role="historyKey"><%=list[i].title%></span>
          <%if(list[i].region){%>
            <span class="msgListArea"><%=list[i].region%></span>
          <%}%>
        </span>
        <%if(type === 'sell'){%>
          <span class="msgListAdd">约<%=list[i].count%>套在售</span>
        <%}else if(type === 'deal'){%>
          <span class="msgListAdd">约<%=list[i].count%>套成交</span>
        <%}%>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="savedSearchTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">已保存搜索</span>
    <div class="searchMsgTitleRightPart">
    <%if(totalCount){%>
      <a class="totalNew">查看<%=totalCount%>套新增房源</a>
    <%}%>
      <a href="<%=userCenterUrl%>" class="manage">管理</a>
    </div>
  </div>
  <ul data-bl="sug" data-el="history">
    <%for(var i = 0; i < savedData.length; i++){
      var title = savedData[i].query ? savedData[i].query + '&nbsp;' : '';
      title = title + savedData[i].title.join('&nbsp;');
    %>
      <li>
        <a href="<%=savedData[i].url%>" role="savedSearch" data-log_index="<%=i+1%>" data-log_value="<%=title%>" class="sug--search_item">
          <span class="msgListTitle"><%=title%></span>
          <%if(savedData[i].unread && savedData[i].unread !== 0){%>
          <span class="msgListAdd">新增<%=savedData[i].unread%>套</span>
          <%}%>
        </a>
      </li>
    <%}%>
  </ul>
</script>

<script>
  var hotSearchData = {
    channel:[{"name":"\u4e8c\u624b\u623f","action":"ershoufang","channel":"ershoufang","checked":1,"tipsHot":{"query":[{"string":"\u7fe0\u82d1\u4e09\u533a","url":"http:\/\/hz.lianjia.com\/ershoufang\/c1811043641797\/"},{"string":"\u95f8\u5f04\u53e3","url":"http:\/\/hz.lianjia.com\/ditiefang\/li110460707s100021558\/"},{"string":"\u6587\u6cfd\u8def","url":"http:\/\/hz.lianjia.com\/ditiefang\/li110460707s100022353\/"},{"string":"\u706b\u8f66\u4e1c\u7ad9","url":"http:\/\/hz.lianjia.com\/ditiefang\/li110460707s100021557\/"},{"string":"\u4e07\u5bb6\u82b1\u57ce","url":"http:\/\/hz.lianjia.com\/ershoufang\/c1811043636779\/"},{"string":"\u5609\u7eff\u5317\u82d1","url":"http:\/\/hz.lianjia.com\/ershoufang\/c1811043641701\/"},{"string":"\u671d\u6656\u4e03\u533a","url":"http:\/\/hz.lianjia.com\/ershoufang\/c1811043642571\/"},{"string":"\u9999\u6a1f\u516c\u5bd3","url":"http:\/\/hz.lianjia.com\/ershoufang\/c1811043641392\/"}],"tips":"\u8bf7\u8f93\u5165\u533a\u57df\u3001\u5546\u5708\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"}},{"name":"\u5c0f\u533a","action":"xiaoqu","channel":"xiaoqu","checked":0,"tipsHot":{"query":[{"string":"\u4e16\u7eaa\u65b0\u57ce","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811044030452\/"},{"string":"\u73b0\u4ee3\u540d\u82d1","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811043642566\/"},{"string":"\u4fe1\u4e49\u574a","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811044013109\/"},{"string":"\u73b0\u4ee3\u96c5\u82d1","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811043642567\/"},{"string":"\u7fe0\u82d1\u4e94\u533a","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811043641799\/"},{"string":"\u91d1\u8272\u84dd\u5ead","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811044027397\/"},{"string":"\u7fe0\u82d1\u4e00\u533a","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811043641800\/"},{"string":"\u5357\u90fd\u82b1\u56ed","url":"http:\/\/hz.lianjia.com\/xiaoqu\/1811046016445\/"}],"tips":"\u8bf7\u8f93\u5165\u5c0f\u533a\u540d\u5f00\u59cb\u67e5\u627e\u5c0f\u533a"}},{"name":"\u65b0\u623f","action":"loupan","channel":"xinfang","checked":0,"tipsHot":{"query":[],"tips":"\u8bf7\u8f93\u5165\u697c\u76d8\u540d\u79f0\u5f00\u59cb\u627e\u623f"}},{"name":"\u79df\u623f","action":"zufang","channel":"zufang","checked":0,"tipsHot":{"query":[{"string":"\u671d\u6656\u56db\u533a","url":"http:\/\/hz.lianjia.com\/zufang\/c1811043642513\/"},{"string":"\u7a3b\u9999\u56ed","url":"http:\/\/hz.lianjia.com\/zufang\/c1811043642516\/"},{"string":"\u897f\u6e56\u6587\u5316\u5e7f\u573a","url":"http:\/\/hz.lianjia.com\/ditiezufang\/li110460707s100021560\/"},{"string":"\u95f8\u5f04\u53e3","url":"http:\/\/hz.lianjia.com\/ditiezufang\/li110460707s100021558\/"},{"string":"\u6253\u94c1\u5173","url":"http:\/\/hz.lianjia.com\/ditiezufang\/li110460707s100021559\/"},{"string":"\u73b0\u4ee3\u96c5\u82d1","url":"http:\/\/hz.lianjia.com\/zufang\/c1811043642567\/"}],"tips":"\u8bf7\u8f93\u5165\u533a\u57df\u3001\u5546\u5708\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"}},{"name":"\u7ecf\u7eaa\u4eba","action":"jingjiren","channel":"jingjiren","checked":0,"tipsHot":{"query":[],"tips":"\u8bf7\u8f93\u5165\u5546\u5708\u3001\u5c0f\u533a\u6216\u7ecf\u7eaa\u4eba\u7684\u59d3\u540d\u3001\u7535\u8bdd..."}}],
    curChannel:'ershoufang'
  };
</script>
<div class="m-filter">
      <div class="position">
      <dl>
        <h2><dt title="杭州成交位置">位置</dt></h2>
        <dd>
                  <a href="/chengjiao/" class="selected" title="杭州成交区域">
            区域<span class="arrow"></span>
          </a>
                </dd>
      </dl>
      <dl>
        <dt></dt>
        <dd>
          <!-- 区域 -->
                    <div data-role="ershoufang" >
            <div>
                              <a href="/chengjiao/xihu/"  title="杭州西湖成交二手房 ">西湖</a>
                              <a href="/chengjiao/xiacheng/"  title="杭州下城成交二手房 ">下城</a>
                              <a href="/chengjiao/jianggan/"  title="杭州江干成交二手房 ">江干</a>
                              <a href="/chengjiao/gongshu/"  title="杭州拱墅成交二手房 ">拱墅</a>
                              <a href="/chengjiao/shangcheng/"  title="杭州上城成交二手房 ">上城</a>
                              <a href="/chengjiao/binjiang/"  title="杭州滨江成交二手房 ">滨江</a>
                              <a href="/chengjiao/yuhang/"  title="杭州余杭成交二手房 ">余杭</a>
                              <a href="/chengjiao/xiaoshan/"  title="杭州萧山成交二手房 ">萧山</a>
                              <a href="/chengjiao/xiasha/"  title="杭州下沙成交二手房 ">下沙</a>
                          </div>
                      </div>
                    <!-- 地铁 -->
                    <!-- 学区 -->
                  </dd>
      </dl>
    </div>
  
  <div class="list-more">
                                                                                                                                                                                                                        <dl class=" hasmore" >
          <h2><dt title="杭州售价成交二手房">售价</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/p1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">100万以下</span>
                              </a>
                                                                    <a href="/chengjiao/p2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">100-150万</span>
                              </a>
                                                                    <a href="/chengjiao/p3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">150-200万</span>
                              </a>
                                                                    <a href="/chengjiao/p4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">200-300万</span>
                              </a>
                                                                    <a href="/chengjiao/p5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">300-500万</span>
                              </a>
                                                                    <a href="/chengjiao/p6/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">500万以上</span>
                              </a>
                                                              <span class="customFilter mt" data-role="price">
                <input type="text" role="minValue" value="">
                <span>-</span>
                <input type="text" role="maxValue" value="">&nbsp;
                                  <span>万</span>
                                <button class="btn-range hide" data-url="/chengjiao/bp{min}ep{max}/">确定</button>
              </span>
                                                  <span class="btn-showmore">+ 更多及自定义</span>
                      </dd>
        </dl>
                                                                                                                                                                                                                                  <dl class=" hasmore" >
          <h2><dt title="杭州面积成交二手房">面积</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/a1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">50平以下</span>
                              </a>
                                                                    <a href="/chengjiao/a2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">50-70平</span>
                              </a>
                                                                    <a href="/chengjiao/a3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">70-90平</span>
                              </a>
                                                                    <a href="/chengjiao/a4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">90-120平</span>
                              </a>
                                                                    <a href="/chengjiao/a5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">120-140平</span>
                              </a>
                                                                    <a href="/chengjiao/a6/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">140-160平</span>
                              </a>
                                                                    <a href="/chengjiao/a7/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">160-200平</span>
                              </a>
                                                                    <a href="/chengjiao/a8/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">200平以上</span>
                              </a>
                                                              <span class="customFilter mt" data-role="area">
                <input type="text" role="minValue" value="">
                <span>-</span>
                <input type="text" role="maxValue" value="">&nbsp;
                                  <span>平</span>
                                <button class="btn-range hide" data-url="/chengjiao/ba{min}ea{max}/">确定</button>
              </span>
                                                  <span class="btn-showmore">+ 更多及自定义</span>
                      </dd>
        </dl>
                                                                                                                                                          <dl class=" " >
          <h2><dt title="杭州房型成交二手房">房型</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/l1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">一室</span>
                              </a>
                                                                    <a href="/chengjiao/l2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">二室</span>
                              </a>
                                                                    <a href="/chengjiao/l3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">三室</span>
                              </a>
                                                                    <a href="/chengjiao/l4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">四室</span>
                              </a>
                                                                    <a href="/chengjiao/l5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">四室以上</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                        <dl class="hide " data-role="hide-row">
          <h2><dt title="杭州用途成交二手房">用途</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/sf1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">普通住宅</span>
                              </a>
                                                                    <a href="/chengjiao/sf3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">别墅</span>
                              </a>
                                                                    <a href="/chengjiao/sf4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">四合院</span>
                              </a>
                                                                    <a href="/chengjiao/sf5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">其他</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                      <dl class="hide " data-role="hide-row">
          <h2><dt title="杭州楼层成交二手房">楼层</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/lc1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">低楼层</span>
                              </a>
                                                                    <a href="/chengjiao/lc2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">中楼层</span>
                              </a>
                                                                    <a href="/chengjiao/lc3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">高楼层</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                                          <dl class="hide " data-role="hide-row">
          <h2><dt title="杭州朝向成交二手房">朝向</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/f1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝东</span>
                              </a>
                                                                    <a href="/chengjiao/f2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝南</span>
                              </a>
                                                                    <a href="/chengjiao/f3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝西</span>
                              </a>
                                                                    <a href="/chengjiao/f4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝北</span>
                              </a>
                                                                    <a href="/chengjiao/f5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">南北</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                                          <dl class="hide " data-role="hide-row">
          <h2><dt title="杭州楼龄成交二手房">楼龄</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/y1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">5年以内</span>
                              </a>
                                                                    <a href="/chengjiao/y2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">10年以内</span>
                              </a>
                                                                    <a href="/chengjiao/y3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">15年以内</span>
                              </a>
                                                                    <a href="/chengjiao/y4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">20年以内</span>
                              </a>
                                                                    <a href="/chengjiao/y5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">20年以上</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                      <dl class="hide " data-role="hide-row">
          <h2><dt title="杭州装修成交二手房">装修</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/de1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">精装修</span>
                              </a>
                                                                    <a href="/chengjiao/de2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">普通装修</span>
                              </a>
                                                                    <a href="/chengjiao/de3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">毛坯房</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                    <dl class="hide " data-role="hide-row">
          <h2><dt title="杭州电梯成交二手房">电梯</dt></h2>
          <dd>
                                                                    <a href="/chengjiao/ie2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">有电梯</span>
                              </a>
                                                                    <a href="/chengjiao/ie1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">无电梯</span>
                              </a>
                                                          </dd>
        </dl>
                  <dl class="hide otherItem" data-role="hide-row">
      <dt class="other">其他</dt>
      <dd>
      <form id="otherSearchForm">
        <input class="inp-search" type="text" value="" placeholder="在结果中搜索">
        <button type="submit" class="btn-search">确定</button>
      </form>
      </dd>
    </dl>
      </div>
    <div class="more btn-more">更多选项<span class="arrow"></span></div>
  </div>
<div class="content"><!-- 左侧内容 --><div class="leftContent"><div class="orderFilter"><div class="orderTag"><ul><li class='selected'><h3><a href="/chengjiao/">默认排序</span></a></h3></li><li ><h3><a href="/chengjiao/ddo21/">房屋总价</a></h3></li><li ><h3><a href="/chengjiao/ddo31/">房屋单价</a></h3></li><li ><h3><a href="/chengjiao/ddo11/">房屋面积</a></h3></li></ul></div><div class="filterAgain"><div class="title">筛选：</div><ul></ul></div></div><div class="resultDes clear"><div class="total fl">共找到<span> 15187 </span>套杭州成交房源</div><div class="button fr"></div></div><ul class="listContent"><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101114191.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/40214eb4-de7a-410c-bd58-735d967e7f97室.jpg.280x210.jpg" alt="大塘新村 1室1厅 37平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101114191.html" target="_blank">大塘新村 1室1厅 37平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 精装&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>108</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共6层) 1988年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">29190</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线西湖文化广场916米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌115万</span><span>成交周期35天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101210217.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/64a19a2f-e68d-45f1-98c1-a3d6b409cf81.jpg.280x210.jpg" alt="大营盘 1室1厅 30.95平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101210217.html" target="_blank">大营盘 1室1厅 30.95平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>70</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共7层) 板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">22618</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线武林广场1165米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌70万</span><span>成交周期8天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103100921364.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/f1bb2f47-aea7-48db-a035-f3a9934f6ac6.JPG.280x210.jpg" alt="凯德视界 2室1厅 71平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103100921364.html" target="_blank">凯德视界 2室1厅 71平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 精装&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>220</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共18层) 2009年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">30986</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌240万</span><span>成交周期99天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103100904885.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/9289327c-5309-40a0-ae06-10571c6902b5.jpg.280x210.jpg" alt="通和戈雅公寓 3室2厅 136.5平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103100904885.html" target="_blank">通和戈雅公寓 3室2厅 136.5平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 精装&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>264.4</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共5层) 2007年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">19370</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌260万</span><span>成交周期105天</span></span></div></div></li><li><a class="img noPic" href="http://hz.lianjia.com/chengjiao/103101000827.html" target="_blank" rel="nofollow"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101000827.html" target="_blank">现代印象广场 1室1厅 51平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>68</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共30层) 塔楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">13334</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌80万</span><span>成交周期63天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101214530.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/5b71ba76-be1a-48eb-842f-1f0fda64b0d1.jpg.280x210.jpg" alt="伊萨卡国际城浩泽园 3室2厅 106.7平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101214530.html" target="_blank">伊萨卡国际城浩泽园 3室2厅 106.7平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>189</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共34层) 2008年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">17714</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线下沙江滨166米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌185万</span><span>成交周期7天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103100988573.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/93637c7b-ae40-4af9-aa32-7f4f08382dbd.jpg.280x210.jpg" alt="良渚文化村白鹭郡北 3室2厅 130平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103100988573.html" target="_blank">良渚文化村白鹭郡北 3室2厅 130平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 毛坯&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>214</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共5层) 2006年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">16462</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌230万</span><span>成交周期66天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101163231.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/303576af-f1d8-4bf8-9c03-bf63f09063cd.JPG.280x210.jpg" alt="寰宇天下 2室2厅 89平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101163231.html" target="_blank">寰宇天下 2室2厅 89平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>400</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共34层) 2014年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">44944</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线江陵路734米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌410万</span><span>成交周期22天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101202632.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/4a664bc9-f586-4de2-9621-1777d39f172c.jpg.280x210.jpg" alt="大关西三苑 2室1厅 59.5平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101202632.html" target="_blank">大关西三苑 2室1厅 59.5平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>142</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共6层) 板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">23866</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌165万</span><span>成交周期10天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101210139.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/0a0febf9-af5a-4d0b-a510-90a0b67e705e.jpg.280x210.jpg" alt="欣盛东方郡西区 3室2厅 102.08平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101210139.html" target="_blank">欣盛东方郡西区 3室2厅 102.08平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>455</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共6层) 2010年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">44573</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线滨和路349米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌450万</span><span>成交周期8天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101030340.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/9bde3f91-3212-44cd-ab9d-463949f3d784贝.jpg.280x210.jpg" alt="红苹果家园 3室2厅 115平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101030340.html" target="_blank">红苹果家园 3室2厅 115平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>225</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共18层) 板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">19566</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线客运中心1094米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌230万</span><span>成交周期56天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103100890280.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/6cc761f0-3139-4506-87fa-cb23254ecf1e.jpg.280x210.jpg" alt="金帝金色钱塘 4室2厅 139平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103100890280.html" target="_blank">金帝金色钱塘 4室2厅 139平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>340</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共24层) 2010年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">24461</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线滨康路832米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌340万</span><span>成交周期109天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101093431.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/43352e1c-371d-4e8a-b54e-987a27d47650.jpg.280x210.jpg" alt="红街公寓 3室2厅 136平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101093431.html" target="_blank">红街公寓 3室2厅 136平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>406</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共18层) 2010年建塔楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">29853</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距4号线新风684米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌408万</span><span>成交周期40天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101123258.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/1357acaf-249b-4987-8199-bf99b8c3e986室.jpg.280x210.jpg" alt="稻香园北区 2室1厅 73.77平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101123258.html" target="_blank">稻香园北区 2室1厅 73.77平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 简装&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>180</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共7层) 1995年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">24401</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌185万</span><span>成交周期32天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101141442.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/15c814b3-c8b7-451c-bddc-50941e8e896f.JPG.280x210.jpg" alt="云厦连园 2室2厅 86平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101141442.html" target="_blank">云厦连园 2室2厅 86平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>295</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共12层) 2010年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">34303</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线西兴320米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌310万</span><span>成交周期28天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103100975494.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/13508f10-b5fb-472f-be5a-bebff09b9082.jpg.280x210.jpg" alt="德信中外公寓 3室2厅 89.62平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103100975494.html" target="_blank">德信中外公寓 3室2厅 89.62平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 精装&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>262</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共11层) 2013年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">29235</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线金沙湖707米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌265万</span><span>成交周期70天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101108514.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/691cb585-8124-4eef-8003-5b141fa7a752.JPG.280x210.jpg" alt="蚕花园永庆坊 1室1厅 55.59平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101108514.html" target="_blank">蚕花园永庆坊 1室1厅 55.59平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 简装&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>89</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共21层) 2000年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">16011</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌95万</span><span>成交周期36天</span></span></div></div></li><li><a class="img noPic" href="http://hz.lianjia.com/chengjiao/103101168733.html" target="_blank" rel="nofollow"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101168733.html" target="_blank">金帝海珀一期 3室2厅 88.48平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>133</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共30层) 2010年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">15032</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌135万</span><span>成交周期20天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101116959.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/29d8904b-788f-48d6-a548-40be84e5a2303.jpg.280x210.jpg" alt="金帝海珀一期 5室2厅 159.34平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101116959.html" target="_blank">金帝海珀一期 5室2厅 159.34平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>210</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共25层) 2010年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">13180</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌210万</span><span>成交周期34天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101182432.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/965e65f1-e064-4323-8015-0f2cc730cdf8.jpg.280x210.jpg" alt="朗诗国际街区 2室2厅 81.17平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101182432.html" target="_blank">朗诗国际街区 2室2厅 81.17平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>136</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共32层) 2009年建塔楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">16755</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线云水789米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌136万</span><span>成交周期16天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101003419.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/752712ce-95e4-4711-a8e9-0c8a9dca21595.jpg.280x210.jpg" alt="广悦公寓 3室2厅 105.3平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101003419.html" target="_blank">广悦公寓 3室2厅 105.3平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 简装</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>100</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共6层) </div><div class="source">链家成交</div><div class="unitPrice"><span class="number">9497</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌175万</span><span>成交周期62天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101145707.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/46312cb9-a43d-48f7-86a9-99df09de015f.JPG.280x210.jpg" alt="迎春小区 2室1厅 49.04平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101145707.html" target="_blank">迎春小区 2室1厅 49.04平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>145.5</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共5层) 2005年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">29670</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线滨和路501米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌150万</span><span>成交周期26天</span></span></div></div></li><li><a class="img noPic" href="http://hz.lianjia.com/chengjiao/103101162519.html" target="_blank" rel="nofollow"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101162519.html" target="_blank">明园路 2室1厅 47.69平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>88</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共5层) 2000年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">18453</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌88万</span><span>成交周期22天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101202967.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/772a179b-7f2a-496e-99e8-6b5a567dd184.jpg.280x210.jpg" alt="滨江曙光之城 3室2厅 138.69平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101202967.html" target="_blank">滨江曙光之城 3室2厅 138.69平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>400</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共15层) 2011年建塔楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">28842</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌530万</span><span>成交周期9天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101183711.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/75ac75c2-58de-45e7-bbfc-45266b13218d.jpg.280x210.jpg" alt="景芳新五区 2室1厅 61.95平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101183711.html" target="_blank">景芳新五区 2室1厅 61.95平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>209</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共7层) 2000年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">33737</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距4号线景芳291米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌218万</span><span>成交周期15天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101143232.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/874264eb-0e3c-4713-a722-a3ada9069475.jpg.280x210.jpg" alt="紫金公寓 3室2厅 73.98平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101143232.html" target="_blank">紫金公寓 3室2厅 73.98平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>232</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共7层) 1996年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">31360</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌235万</span><span>成交周期27天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101135670.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/a26bdb9a-9868-4b70-8621-a7f40109504f.jpg.280x210.jpg" alt="雅兰公寓 3室2厅 135.79平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101135670.html" target="_blank">雅兰公寓 3室2厅 135.79平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 精装&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>420</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共11层) 2000年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">30931</span>元/平</div></div><div class="dealHouseInfo"><span class="dealHouseIcon"></span><span class="dealHouseTxt"><span>距1号线打铁关781米</span></span></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌468万</span><span>成交周期29天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101206195.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/8e0e3291-af1e-401e-91cc-d9b79f8cd3cb.jpg.280x210.jpg" alt="朝晖九区 2室1厅 60.1平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101206195.html" target="_blank">朝晖九区 2室1厅 60.1平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>西 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>170.5</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共7层) 1993年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">28370</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌175万</span><span>成交周期8天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101210038.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/a5a695f0-0acd-4e1a-905e-ce2926925581.jpg.280x210.jpg" alt="平海路小区 2室1厅 49.65平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101210038.html" target="_blank">平海路小区 2室1厅 49.65平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 北 | 其他&nbsp;| 无电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>205</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共6层) 1989年建板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">41290</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌225万</span><span>成交周期7天</span></span></div></div></li><li><a class="img" href="http://hz.lianjia.com/chengjiao/103101196333.html" target="_blank" rel="nofollow"><img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20170504205919" data-original="http://image1.ljcdn.com/330100-inspection/af8899f1-9559-4903-a0c2-27c302235834.JPG.280x210.jpg" alt="联合格里 3室2厅 86.78平米"></a><div class="info"><div class="title"><a href="http://hz.lianjia.com/chengjiao/103101196333.html" target="_blank">联合格里 3室2厅 86.78平米</a></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>南 | 其他&nbsp;| 有电梯</div><div class="dealDate">2017.04.22</div><div class="totalPrice"><span class='number'>176.5</span>万</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共16层) 板楼</div><div class="source">链家成交</div><div class="unitPrice"><span class="number">20339</span>元/平</div></div><div class="dealCycleeInfo"><span class="dealCycleIcon"></span><span class="dealCycleTxt"><span>挂牌185万</span><span>成交周期11天</span></span></div></div></li></ul><!-- 无搜索结果 --><div class="contentBottom clear" ><div class="crumbs fl"><a href="/">链家网杭州站</a><h1><span >&nbsp;&gt;&nbsp;</span></h1><a href="/chengjiao/">杭州二手房成交价格</a></div><div class="page-box fr"><div class="page-box house-lst-page-box" comp-module='page' page-url="/chengjiao/pg{page}/"page-data='{"totalPage":100,"curPage":1}'></div>


</div></div></div><!-- 右侧sidebar --><div class="rightLayout"><div class="rightContent"><div class="map hide"><div class="pic"></div><button>给自己的房子估价</button></div><div class="wrap-side-content hide" id="wrap-side-content"><div class="price" id="tpl-r-price"></div><div class="suggestCommunity" id="tpl-r-house"></div><div class="wenda zixun" id="tpl-r-redian"></div><div class="wenda" id="tpl-r-wenda"></div></div></div></div></div><div class="footer"><div class="wrapper"><div class="f-title"><div class="fl"><ul><li><a href="http://www.lianjia.com/zhuanti/home/" target="_blank">了解链家网</a></li><li><a href="http://hz.lianjia.com/about/aboutlianjia/" rel="nofollow" target="_blank">关于链家</a></li><li><a href="http://hz.lianjia.com/about/contactus/" rel="nofollow" target="_blank">联系我们</a></li><li><a href="http://join.lianjia.com/" rel="nofollow" target="_blank">加入我们</a></li><li><a href="http://www.lianjia.com/privacy/" rel="nofollow" target="_blank">隐私声明</a></li><li><a href="http://hz.lianjia.com/sitemap/" target="_blank">网站地图</a></li><li><a href="http://www.lianjia.com/notice/7.html" target="_blank">友情链接</a></li><li><a href="http://agent.lianjia.com/" rel="nofollow" target="_blank">经纪人登录</a></li></ul></div><div class="fr">官方客服 1010 9666</div></div><div class="lianjia-link-box"><div class="fl"><div class="tab"><span  class="hover">热门城市二手房</span><span >热门城市租房网</span><span >热门城市楼盘</span><span >热门百科</span></div><div class="link-list"><div><dd><a target="_blank" href="http://bj.lianjia.com/ershoufang/">北京二手房</a><a target="_blank" href="http://gz.lianjia.com/ershoufang/">广州二手房</a><a target="_blank" href="http://sz.lianjia.com/ershoufang/">深圳二手房</a><a target="_blank" href="http://tj.lianjia.com/ershoufang/">天津二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/">成都二手房</a><a target="_blank" href="http://nj.lianjia.com/ershoufang/">南京二手房</a><a target="_blank" href="http://hz.lianjia.com/ershoufang/">杭州二手房</a><a target="_blank" href="http://qd.lianjia.com/ershoufang/">青岛二手房</a><a target="_blank" href="http://dl.lianjia.com/ershoufang/">大连二手房</a><a target="_blank" href="http://xm.lianjia.com/ershoufang/">厦门二手房</a><a target="_blank" href="http://wh.lianjia.com/ershoufang/">武汉二手房</a><a target="_blank" href="http://cq.lianjia.com/ershoufang/">重庆二手房</a><a target="_blank" href="http://cs.lianjia.com/ershoufang/">长沙二手房</a><a target="_blank" href="http://jn.lianjia.com/ershoufang/">济南二手房</a></dd></div><div><dd><a target="_blank" href="http://bj.lianjia.com/zufang/">北京租房</a><a target="_blank" href="http://gz.lianjia.com/zufang/">广州租房</a><a target="_blank" href="http://sz.lianjia.com/zufang/">深圳租房</a><a target="_blank" href="http://tj.lianjia.com/zufang/">天津租房</a><a target="_blank" href="http://cd.lianjia.com/zufang/">成都租房</a><a target="_blank" href="http://nj.lianjia.com/zufang/">南京租房</a><a target="_blank" href="http://hz.lianjia.com/zufang/">杭州租房</a><a target="_blank" href="http://qd.lianjia.com/zufang/">青岛租房</a><a target="_blank" href="http://dl.lianjia.com/zufang/">大连租房</a><a target="_blank" href="http://xm.lianjia.com/zufang/">厦门租房</a><a target="_blank" href="http://wh.lianjia.com/zufang/">武汉租房</a><a target="_blank" href="http://cq.lianjia.com/zufang/">重庆租房</a><a target="_blank" href="http://cs.lianjia.com/zufang/">长沙租房</a><a target="_blank" href="http://jn.lianjia.com/zufang/">济南租房</a></dd></div><div><dd><a target="_blank" href="//sh.fang.lianjia.com/">北京楼盘</a><a target="_blank" href="//tj.fang.lianjia.com/">天津楼盘</a><a target="_blank" href="//nj.fang.lianjia.com/">南京楼盘</a><a target="_blank" href="//cd.fang.lianjia.com/">成都楼盘</a><a target="_blank" href="//dl.fang.lianjia.com/">大连楼盘</a><a target="_blank" href="//qd.fang.lianjia.com/">青岛楼盘</a><a target="_blank" href="//hz.fang.lianjia.com/">杭州楼盘</a><a target="_blank" href="//wh.fang.lianjia.com/">武汉楼盘</a><a target="_blank" href="//sz.fang.lianjia.com/">深圳楼盘</a><a target="_blank" href="//cq.fang.lianjia.com/">重庆楼盘</a><a target="_blank" href="//cs.fang.lianjia.com/">长沙楼盘</a><a target="_blank" href="//xa.fang.lianjia.com/">西安楼盘</a><a target="_blank" href="//jn.fang.lianjia.com/">济南楼盘</a><a target="_blank" href="//sjz.fang.lianjia.com/">石家庄楼盘</a></dd></div><div><dd><a target="_blank" href="//news.lianjia.com/cd/baike/011207.html">绿地率和绿化率对比</a><a target="_blank" href="//news.lianjia.com/cd/baike/010664.html">买卖小产权房风险</a><a target="_blank" href="//news.lianjia.com/cd/baike/010530.html">房屋产权核验要素</a><a target="_blank" href="//news.lianjia.com/bj/baike/033371.html">如何选择换房方案</a><a target="_blank" href="//news.lianjia.com/bj/baike/06645.html">卖房收款项</a><a target="_blank" href="//news.lianjia.com/bj/baike/029526.html">买两限房注意事项</a><a target="_blank" href="//news.lianjia.com/bj/baike/017029.html">卖房补充协议</a><a target="_blank" href="//news.lianjia.com/bj/baike/027738.html">租房物业交割</a><a target="_blank" href="//news.lianjia.com/bj/baike/019792.html">二手房资金监管</a><a target="_blank" href="//news.lianjia.com/bj/baike/017745.html">通州二手房限购政策</a><a target="_blank" href="//news.lianjia.com/bj/baike/06607.html">新房装修注意事项</a><a target="_blank" href="//news.lianjia.com/dl/baike/09536.html">大连购房奖励领取</a><a target="_blank" href="//news.lianjia.com/dl/baike/06682.html">买房公证类型</a><a target="_blank" href="//news.lianjia.com/dl/baike/025723.html">房屋法定继承顺序</a><a target="_blank" href="//news.lianjia.com/dl/baike/030230.html">大连购房提取公积金</a><a target="_blank" href="//news.lianjia.com/dl/baike/09438.html">大连二手房购买流程</a><a target="_blank" href="//news.lianjia.com/dl/baike/049312.html">二手房个人所得税</a><a target="_blank" href="//news.lianjia.com/dl/baike/054567.html">新房得房率计算</a><a target="_blank" href="//news.lianjia.com/dl/baike/032782.html">商业贷款银行拒贷</a><a target="_blank" href="//news.lianjia.com/dl/baike/052395.html">大连买房落户</a><a target="_blank" href="//news.lianjia.com/tj/baike/010503.html">买新房二手房区别</a><a target="_blank" href="//news.lianjia.com/tj/baike/010865.html">二手房买卖交易流程</a><a target="_blank" href="//news.lianjia.com/tj/baike/09968.html">物业交割清算费用</a><a target="_blank" href="//news.lianjia.com/tj/baike/017136.html">二手房交定金注意事项</a><a target="_blank" href="//news.lianjia.com/tj/baike/011251.html">二手房遗留物业费</a><a target="_blank" href="//news.lianjia.com/tj/baike/011420.html">二手房物业交割步骤</a><a target="_blank" href="//news.lianjia.com/sjz/baike/0102291.html">规避租房合同纠纷</a><a target="_blank" href="//news.lianjia.com/sjz/baike/099896.html">农村房产买卖政策</a><a target="_blank" href="//news.lianjia.com/sjz/baike/099157.html">套内建筑面积</a><a target="_blank" href="//news.lianjia.com/sjz/baike/098358.html">规避查房封房风险</a><a target="_blank" href="//news.lianjia.com/sjz/baike/098105.html">老房子采光改造</a><a target="_blank" href="//news.lianjia.com/sjz/baike/097456.html">好户型实例解析</a><a target="_blank" href="//news.lianjia.com/sjz/baike/030648.html">委托买房核实真假</a><a target="_blank" href="//news.lianjia.com/sjz/baike/038797.html">委托中介买房环节</a><a target="_blank" href="//news.lianjia.com/sjz/baike/033364.html">购房意向定金退还</a><a target="_blank" href="//news.lianjia.com/sjz/baike/033385.html">买安置房风险</a><a target="_blank" href="//news.lianjia.com/sjz/baike/018776.html">石家庄住房公积金提取</a><a target="_blank" href="//news.lianjia.com/sjz/baike/08331.html">办理房产继承公证</a><a target="_blank" href="//news.lianjia.com/cd/baike/040041.html">小户型的装修技巧</a><a target="_blank" href="//news.lianjia.com/sjz/baike/098088.html">水路验收标准</a></dd></div></div></div><div class="clear"></div></div><div class="bottom"><div class="copyright fl">北京链家房地产经纪有限公司 | 网络经营许可证 京ICP备11024601号-12 | © Copyright©2010-2017 链家网Lianjia.com版权所有</div></div></div></div>

<script src="http://s1.ljcdn.com/feroot/pc/asset/base/fe.js?_v=20170504205919"></script><script src="http://s1.ljcdn.com/feroot/pc/asset/common/common.js?_v=20170504205919"></script><div style="display:none"><script src="http://s1.ljcdn.com/feroot/dep/ljanalytics.js?_v=20170504205919"></script></div><div id="only" data-city="hz" data-page="chengjiao_index"></div>
<script>var path = 'http://s1.ljcdn.com/feroot/pc/asset?_v=20170504205919'.split("?");require.config({baseUrl: path[0],paths: {'echarts' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie' : '../../dep/echarts-1.4.1/build/echarts','echarts3' : '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs:  path[1]});var feData = {"cityName": "北京","getFavHouseUrl":       "/api/gethousefav","setFavHouseUrl":       "/api/sethousefav","getLastSearch":        "/api/getlastsearch","getCommunityHistory":  "/api/getcommunityhistory","verifyHouse":          "/api/verifyHouse","getUser":              "/api/getUser","verifyCode":           "/api/getVerifyCode","complaint":            "/api/complaint","getDecoration":        "/api/getDecoration","trendData" :           "/site/getpicinfo"}</script>
<!-- 价格 -->
<script type="text/template" id="priceSideBarTpl">
<%if(tag !== 'school'){%>
  <div class="title"><%=name%>最新参考均价</div>
  <div class="priceMap" id="priceChartContainer"></div>
  <a href="<%=fangjia_url%>" class="unitPrice" target="_blank">
    <span><%=month_trans%></span>元/平米
  </a>
  <div class="info">
    <a href="<%=fangjia_url%>" target="_blank">环比上月均价<%=month_trans_ratio>=0?'上涨':'下降'%> <%=month_trans_ratio%>%</a>
    <a href="<%=chengjiao_url%>" target="_blank">/ 近90天成交<%=sold_90_day%>套</a>
    <%if(tag === '小区'){%>
    <div>
      <a class="cardMoreDetail" href="<%=url%>" target="_blank">查看小区详情>></a>
    </div>
    <%}%>
  </div>
<%}else{%>
  <a class="title" href="<%=url%>" target="_blank"><%=name%></a>
  <div class="unitPrice school">
    <span><%=min_unit_price%></span>万元起
  </div>
  <div class="info">
    <a href="<%=url%>" target="_blank">本学区目前有在售二手房<%=sell_num%>套，划片小区<%=resblock_nums%>个</a>
    <a class="cardMoreDetail" href="<%=url%>"  target="_blank">查看学区详情>></a>
  </div>
<%}%>
</script>

<!-- 在售小区 -->
<script type="text/template" id="tpl-house">
  <div class="title">本小区在售</div>
  <ul>
    <%for(var i = 0; i < list.length; i++){var item=list[i];%>
      <li>
        <a class="img" href="<%=item.viewUrl%>" target="_blank">
          <img src="<%=item.pic_url%>">
          <div class="price"><%=item.price%>万</div>
        </a>
        <div class="info">
          <a href="<%=item.viewUrl%>" target="_blank"><%=item.title%></a>
          <b><%=item.room%> / <%=item.area%>平</b>
        </div>
      </li>
    <%}%>
  </ul>
</script>
<!-- 热点 -->
<script type="text/template" id="tpl-redian">
  <div class="title">热点精选</div>
  <ul>
    <%for(var i=0;i<list.length;i++) { var item=list[i];%>
      <li>
        <i class="opt<%=i%>"><%=i+1%></i><a class="info" href="<%=item.url%>" title="<%=item.question_title%>" target="_blank"><%=item.question_title%></a>
      </li>
    <%}%>
  </ul>
</script>
<!-- wenda -->
<script type="text/template" id="tpl-wenda">
  <div class="title">热门问答</div>
  <ul>
    <%for(var i=0;i<list.length;i++) { var item=list[i];%>
      <li>
        <a class="info" href="<%=item.url%>" title="<%=item.question_description%>" target="_blank"><%=item.question_title%></a>
        <span class="time"><%=item.mtime%></span>
      </li>
    <%}%>
  </ul>
</script>


<script type="text/javascript">
require(['ershoufang/dealList/index'], function (main) {
  main({
    sidebar:{"type":"city","cityId":330100,"uuid":"0d75b879-1385-49c9-af21-b6606d3b550e","ucid":null,"id":330100},
    SIRKeyword:"",
    filterBar:[]
  });

  var logMsg = $("[log-mod='laobi_spellcheck']");

  if(logMsg.length) {

    function fixUrl(originUrl, prefixStr) {
        if(originUrl.search(/\?/) > -1) {
            return [originUrl, prefixStr].join("&");
        }

        return [originUrl, prefixStr].join("?");
    }

    logMsg.each(function(ka, va) {
        var ret = [];
        var $el = $(this);

        $el.find("a").each(function(k, v) {

            $(this).attr("href", fixUrl($(this).attr("data-origin_url"), 'from_mod=spellcheck'));

            ret.push($(this).text());
        });

        UT.send({
            type: 'show',
            subtype: 'module_show',
            el: ret.join('---')
        }, $el.get(0));

        UT.send({
            type: 'show',
            subtype: 'module_show',
            mod: [$el.attr("log-mod"), $el.attr("log-mod_description")].join("_"),
            bl: $el.attr("data-bl"),
            el: ret.join('---'),
            value: $el.attr("data-log_value"),
            index: ''
        });

        $el.on("mousedown", "a", function() {
            var $m = $(this);

            UT.send({
                type: 'click',
                subtype: 'link',
                mod: [$el.attr("log-mod"), $el.attr("log-mod_description")].join("_"),
                bl: $m.attr("data-bl"),
                el: $m.attr("data-el"),
                value: $m.attr("data-log_value"),
                index: $m.attr("data-log_index"),
                url: $m.get(0).getAttribute("href", 2)
            });
        });
    });

  }

});
require(['common/backtopV3'], function (main) {
  main({
    ucid: '',
    uuid: '0d75b879-1385-49c9-af21-b6606d3b550e',
    loadingImg: 'http://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellDetail/img/loading.gif?_v=20170504205919',
    qrImg: '//ajax.api.lianjia.com/qr/getDownloadQr'
  });
});

</script>
<script>require(['common/suggestion'], function (suggestion) {window.defaultSuggest = suggestion.init({requestOptions: {cityId: '330100',cityName: '杭州'},url: '/api/headerSearch?channel=chengjiao&q=',main: '#keyword-box',appendTo: '#suggest-cont',redirect: true});});</script><div class="loninContaner"><div class="overlay_bg"></div><div class="panel_login animated" id="dialog"><div class="panel_info"><div class="panel_tab"><div class="title"><div class="fl">用户登录</div><label class="fr">还没有链家网账号？<a href="//passport.lianjia.com/register/resources/lianjia/register.html?service=http%3A%2F%2Fbj.lianjia.com%2F">马上注册</a></label></div><div class="clear"></div><div id="con_login_user"><form action="" method="post"><ul><li class="show-error"><dd>用户名或密码错误</dd></li><li class="item userName"><i></i><input type="text" class="the_input users" placeholder="请输入手机号" /></li><li class="item pwd"><i></i><input type="password" class="the_input password"  placeholder="请输入登录密码"/></li><li class="item checkVerimg" style="display:none;"><i></i><input type="text" class="the_input ver-img" maxlength="4"  placeholder="请输入验证码"/><img class="verImg"></li><li class="li_01"><label><input type="checkbox" name="remember" value="1" class="mind-login" checked>下次自动登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/">找回密码</a></li><li><a class="login-user-btn"  />立即登录</a></li></ul></form></div><div id="con_login_agent" class="undis"><form action="" method="post"><ul><li class="item"><dd></dd><input type="text" class="the_input users" placeholder="输入经纪人ID号码" /></li><li class="item"><input type="password" class="the_input password"  placeholder="登录密码"/></li><li class="li_01"><label><input type="checkbox" name="remember" value="1" class="mind-login">下次自动登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/">找回密码</a></li><li><input class="login-agent-btn" value="立即登录"/></li></ul></form></div></div></div><div class="registered"></div></div></div><!-- LianjiaIM Style --><link property='stylesheet' rel="stylesheet" href="http://s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?_v=20170504205919"/><script src="//s1.ljcdn.com/web-im-sdk/static/0.9/ljim-core.min.js?_v=20170507"></script><script>(function() {var imConf = {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"};$.listener.on('userInfo', function (data) {if (data.code === 1) {data.ucid = '';}require(['lianjiaIM/lianjiaim'], function (LianjiaIM) {var ljim = new LianjiaIM({appid: imConf.imAppid,appkey: imConf.imAppkey,userData: data,staticRoot: 'http://s1.ljcdn.com/feroot/?_v=20170504205919'});});});})();</script><script type="text/javascript">var advert = 'http://s1.ljcdn.com/feroot/pc/asset/common/advert.js?_v=20170504205919';
    $.listener.on('userInfo', function (data) {
      window.loginData = data;
    });
    var mvl = document.createElement('script');
    mvl.type = 'text/javascript';
    mvl.async = true;
    mvl.src = advert;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(mvl, s);
  </script><script type="text/javascript">(function(){var bp = document.createElement('script');var curProtocol = window.location.protocol.split(':')[0];if (curProtocol === 'https'){bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';} else {bp.src = 'http://push.zhanzhang.baidu.com/push.js';}var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(bp, s);})();</script></body></html>

'''
from scrapy.selector import Selector
from lxml import etree

# dom = etree.HTML(html)

# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a')[0]
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[2]/div[1]/text()')
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[3]/div[1]/text()')
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[4]/span[2]/span/text()')
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[5]/span[2]/span[1]/text()')
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[5]/span[2]/span[2]/text()')
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[2]/div[2]')[0].text
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[3]/div[2]')[0].text
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[2]/div[3]/span')[0].text
# print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[3]/div[3]/span')[0].text

dom = Selector(text=html)

print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a/text()')[0].extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[2]/div[1]/text()').extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[3]/div[1]/text()').extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[4]/span[2]/span/text()').extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[5]/span[2]/span[1]/text()').extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[5]/span[2]/span[2]/text()').extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[2]/div[2]/text()')[0].extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[3]/div[2]/text()')[0].extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[2]/div[3]/span/text()')[0].extract()
print dom.xpath('/html/body/div[4]/div[1]/ul/li[1]/div/div[3]/div[3]/span/text()')[0].extract()






















