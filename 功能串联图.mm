
<map>
  <node ID="root" TEXT="开始">
    <node TEXT="login.py" ID="26TcRmSFEM" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Elogin.py%3C/span%3E" STYLE="bubble" POSITION="default">
      <node TEXT="游客访问" ID="qLHk0JMqym" _mubu_text="%3Cspan%3E%E6%B8%B8%E5%AE%A2%E8%AE%BF%E9%97%AE%3C/span%3E" STYLE="fork">
        <node TEXT="guest_main.py" ID="q9DZ2EXtKe" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Eguest_main.py%3C/span%3E" STYLE="fork">
          <node TEXT="选择返回登录则进入登录界面" ID="BCzHk15Zw7" _mubu_text="%3Cspan%3E%E9%80%89%E6%8B%A9%E8%BF%94%E5%9B%9E%E7%99%BB%E5%BD%95%E5%88%99%E8%BF%9B%E5%85%A5%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork"/>
          <node TEXT="输入信息可以点击提交订单" ID="9EE16MgotA" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E4%BF%A1%E6%81%AF%E5%8F%AF%E4%BB%A5%E7%82%B9%E5%87%BB%E6%8F%90%E4%BA%A4%E8%AE%A2%E5%8D%95%3C/span%3E" STYLE="fork"/>
          <node TEXT="点击查询订单进入查询订单界面" ID="2q0wSPxjJM" _mubu_text="%3Cspan%3E%E7%82%B9%E5%87%BB%E6%9F%A5%E8%AF%A2%E8%AE%A2%E5%8D%95%E8%BF%9B%E5%85%A5%E6%9F%A5%E8%AF%A2%E8%AE%A2%E5%8D%95%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork">
            <node TEXT="" ID="GVg2iVtKxm" _mubu_text="" STYLE="fork">
              <node TEXT="考虑到游客和用户对于快递的查询都只能通过快递单号查询，所以他们都统一进入这个界面（user_search_delivery.py）" ID="j0q8tOJ8Vx" _mubu_text="%3Cspan%3E%E8%80%83%E8%99%91%E5%88%B0%E6%B8%B8%E5%AE%A2%E5%92%8C%E7%94%A8%E6%88%B7%E5%AF%B9%E4%BA%8E%E5%BF%AB%E9%80%92%E7%9A%84%E6%9F%A5%E8%AF%A2%E9%83%BD%E5%8F%AA%E8%83%BD%E9%80%9A%E8%BF%87%E5%BF%AB%E9%80%92%E5%8D%95%E5%8F%B7%E6%9F%A5%E8%AF%A2%EF%BC%8C%E6%89%80%E4%BB%A5%E4%BB%96%E4%BB%AC%E9%83%BD%E7%BB%9F%E4%B8%80%E8%BF%9B%E5%85%A5%E8%BF%99%E4%B8%AA%E7%95%8C%E9%9D%A2%EF%BC%88%3C/span%3E%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_search_delivery.py%3C/span%3E%3Cspan%3E%EF%BC%89%3C/span%3E" STYLE="fork"/>
            </node>
          </node>
        </node>
      </node>
      <node TEXT="注册" ID="Y7rbDPrl2T" _mubu_text="%3Cspan%3E%E6%B3%A8%E5%86%8C%3C/span%3E" STYLE="fork">
        <node TEXT="register.py" ID="nOSRcofRcj" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Eregister.py%3C/span%3E" STYLE="fork">
          <node TEXT="成功注册后进入登录界面" ID="1LtUDXqQNy" _mubu_text="%3Cspan%3E%E6%88%90%E5%8A%9F%E6%B3%A8%E5%86%8C%E5%90%8E%E8%BF%9B%E5%85%A5%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="登录" ID="AwrdLAI9oy" _mubu_text="%3Cspan%3E%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
        <node TEXT="根据账号首位判断身份" ID="6KDXSKNSZ3" _mubu_text="%3Cspan%3E%E6%A0%B9%E6%8D%AE%E8%B4%A6%E5%8F%B7%E9%A6%96%E4%BD%8D%E5%88%A4%E6%96%AD%E8%BA%AB%E4%BB%BD%3C/span%3E" STYLE="fork">
          <node TEXT="普通用户登录" ID="1rEv9SBGzS" _mubu_text="%3Cspan%3E%E6%99%AE%E9%80%9A%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
            <node TEXT="进入主界面" ID="BkoPasK8sz" _mubu_text="%3Cspan%3E%E8%BF%9B%E5%85%A5%E4%B8%BB%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork">
              <node TEXT="user_main.py" ID="fhASQwxLon" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_main.py%3C/span%3E" STYLE="fork">
                <node TEXT="退出登录" ID="qZ63IzL0RP" _mubu_text="%3Cspan%3E%E9%80%80%E5%87%BA%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
                  <node TEXT="回退到登录界面即可" ID="150QFP5lWH" _mubu_text="%3Cspan%3E%E5%9B%9E%E9%80%80%E5%88%B0%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E5%8D%B3%E5%8F%AF%3C/span%3E" STYLE="fork"/>
                </node>
                <node TEXT="修改个人信息" ID="KrW1KHJWOg" _mubu_text="%3Cspan%3E%E4%BF%AE%E6%94%B9%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                  <node TEXT="user_modify_info.py" ID="ItmTtoO1gM" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_modify_info.py%3C/span%3E" STYLE="fork">
                    <node TEXT="输入新密码旧密码点击修改密码" ID="GyqgmG5gaj" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E6%96%B0%E5%AF%86%E7%A0%81%E6%97%A7%E5%AF%86%E7%A0%81%E7%82%B9%E5%87%BB%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81%3C/span%3E" STYLE="fork">
                      <node TEXT="弹窗修改成功与否" ID="0JQMDOs5CN" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E4%BF%AE%E6%94%B9%E6%88%90%E5%8A%9F%E4%B8%8E%E5%90%A6%3C/span%3E" STYLE="fork"/>
                    </node>
                    <node TEXT="输入旧手机号新手机号点击修改手机号" ID="D2xJx4V71A" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E6%97%A7%E6%89%8B%E6%9C%BA%E5%8F%B7%E6%96%B0%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%82%B9%E5%87%BB%E4%BF%AE%E6%94%B9%E6%89%8B%E6%9C%BA%E5%8F%B7%3C/span%3E" STYLE="fork">
                      <node TEXT="弹窗修改成功与否" ID="PbboZnKHx7" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E4%BF%AE%E6%94%B9%E6%88%90%E5%8A%9F%E4%B8%8E%E5%90%A6%3C/span%3E" STYLE="fork"/>
                    </node>
                    <node TEXT="点击查看地址簿信息" ID="9lQI9Gp8N0" _mubu_text="%3Cspan%3E%E7%82%B9%E5%87%BB%E6%9F%A5%E7%9C%8B%E5%9C%B0%E5%9D%80%E7%B0%BF%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                      <node TEXT="address_book.py" ID="Lzbwsu0BGV" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Eaddress_book.py%3C/span%3E" STYLE="fork">
                        <node TEXT="选择列表中的某一数据" ID="z0XgBjlz8m" _mubu_text="%3Cspan%3E%E9%80%89%E6%8B%A9%E5%88%97%E8%A1%A8%E4%B8%AD%E7%9A%84%E6%9F%90%E4%B8%80%E6%95%B0%E6%8D%AE%3C/span%3E" STYLE="fork">
                          <node TEXT="修改" ID="etiHnNMonj" _mubu_text="%3Cspan%3E%E4%BF%AE%E6%94%B9%3C/span%3E" STYLE="fork">
                            <node TEXT="弹窗修改成功与否" ID="h0gckFwCpB" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E4%BF%AE%E6%94%B9%E6%88%90%E5%8A%9F%E4%B8%8E%E5%90%A6%3C/span%3E" STYLE="fork"/>
                          </node>
                          <node TEXT="删除" ID="gFfiNCHuQL" _mubu_text="%3Cspan%3E%E5%88%A0%E9%99%A4%3C/span%3E" STYLE="fork">
                            <node TEXT="弹窗删除成功与否" ID="8xP1iKLnnN" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E5%88%A0%E9%99%A4%E6%88%90%E5%8A%9F%E4%B8%8E%E5%90%A6%3C/span%3E" STYLE="fork"/>
                          </node>
                        </node>
                        <node TEXT="点击添加地址簿信息" ID="KHaPuZz0If" _mubu_text="%3Cspan%3E%E7%82%B9%E5%87%BB%E6%B7%BB%E5%8A%A0%E5%9C%B0%E5%9D%80%E7%B0%BF%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                          <node TEXT="add_address_book.py" ID="sqerYaYoXj" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Eadd_address_book.py%3C/span%3E" STYLE="fork">
                            <node TEXT="输入/选择信息点击确认添加" ID="MvdLy9VXET" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5/%E9%80%89%E6%8B%A9%E4%BF%A1%E6%81%AF%E7%82%B9%E5%87%BB%E7%A1%AE%E8%AE%A4%E6%B7%BB%E5%8A%A0%3C/span%3E" STYLE="fork">
                              <node TEXT="弹窗添加成功与否" ID="wEPy3FOAqt" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E6%B7%BB%E5%8A%A0%E6%88%90%E5%8A%9F%E4%B8%8E%E5%90%A6%3C/span%3E" STYLE="fork"/>
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
                <node TEXT="我要查快递" ID="kBUKHLRvcb" _mubu_text="%3Cspan%3E%E6%88%91%E8%A6%81%E6%9F%A5%E5%BF%AB%E9%80%92%3C/span%3E" STYLE="fork">
                  <node TEXT="user_search_delivery.py" ID="m8KPB4BKDs" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_search_delivery.py%3C/span%3E" STYLE="fork">
                    <node TEXT="同对“游客”描述的一致" ID="96hN3t6sMq" _mubu_text="%3Cspan%3E%E5%90%8C%E5%AF%B9%E2%80%9C%E6%B8%B8%E5%AE%A2%E2%80%9D%E6%8F%8F%E8%BF%B0%E7%9A%84%E4%B8%80%E8%87%B4%3C/span%3E" STYLE="fork"/>
                  </node>
                </node>
                <node TEXT="我要寄快递" ID="Vxb3E1uNXg" _mubu_text="%3Cspan%3E%E6%88%91%E8%A6%81%E5%AF%84%E5%BF%AB%E9%80%92%3C/span%3E" STYLE="fork">
                  <node TEXT="user_sendout.py" ID="tSt6rKlmHG" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_sendout.py%3C/span%3E" STYLE="fork">
                    <node TEXT="输入或选择下拉信息" ID="e5w9lJqbgf" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E6%88%96%E9%80%89%E6%8B%A9%E4%B8%8B%E6%8B%89%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                      <node TEXT="提交订单" ID="0A9A56sVPg" _mubu_text="%3Cspan%3E%E6%8F%90%E4%BA%A4%E8%AE%A2%E5%8D%95%3C/span%3E" STYLE="fork">
                        <node TEXT="弹窗提示结果" ID="JWN9SZ4m6b" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E6%8F%90%E7%A4%BA%E7%BB%93%E6%9E%9C%3C/span%3E" STYLE="fork"/>
                      </node>
                    </node>
                    <node TEXT="返回主界面" ID="6sj2QOCoJW" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%E4%B8%BB%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork"/>
                  </node>
                </node>
                <node TEXT="我收的" ID="y5mxde38TQ" _mubu_text="%3Cspan%3E%E6%88%91%E6%94%B6%E7%9A%84%3C/span%3E" STYLE="fork">
                  <node TEXT="myReceive.py" ID="LmAXKNGxvR" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3EmyReceive.py%3C/span%3E" STYLE="fork">
                    <node TEXT="返回上一级" ID="rC69qcRJnh" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%E4%B8%8A%E4%B8%80%E7%BA%A7%3C/span%3E" STYLE="fork">
                      <node TEXT="返回user_main.py" ID="xtSCOfhBgv" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%3C/span%3E%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_main.py%3C/span%3E" STYLE="fork"/>
                    </node>
                    <node TEXT="选择列表内的某一条信息" ID="JmK9hr6b1q" _mubu_text="%3Cspan%3E%E9%80%89%E6%8B%A9%E5%88%97%E8%A1%A8%E5%86%85%E7%9A%84%E6%9F%90%E4%B8%80%E6%9D%A1%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                      <node TEXT="确认签收" ID="dGPmNlyt1s" _mubu_text="%3Cspan%3E%E7%A1%AE%E8%AE%A4%E7%AD%BE%E6%94%B6%3C/span%3E" STYLE="fork">
                        <node TEXT="弹窗提示结果" ID="4n9o48X87n" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E6%8F%90%E7%A4%BA%E7%BB%93%E6%9E%9C%3C/span%3E" STYLE="fork"/>
                      </node>
                      <node TEXT="拒绝签收" ID="lkChi1yFni" _mubu_text="%3Cspan%3E%E6%8B%92%E7%BB%9D%E7%AD%BE%E6%94%B6%3C/span%3E" STYLE="fork">
                        <node TEXT="弹窗提示结果" ID="7hUYfnfKu9" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E6%8F%90%E7%A4%BA%E7%BB%93%E6%9E%9C%3C/span%3E" STYLE="fork"/>
                      </node>
                    </node>
                  </node>
                </node>
                <node TEXT="我寄的" ID="eS6DuBxd7V" _mubu_text="%3Cspan%3E%E6%88%91%E5%AF%84%E7%9A%84%3C/span%3E" STYLE="fork">
                  <node TEXT="mySend.py" ID="wVMCqjLOJu" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3EmySend.py%3C/span%3E" STYLE="fork">
                    <node TEXT="返回上一级" ID="kNqPczKD2l" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%E4%B8%8A%E4%B8%80%E7%BA%A7%3C/span%3E" STYLE="fork">
                      <node TEXT="返回user_main.py" ID="RcfW6HZuHI" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%3C/span%3E%3Cspan%20class=%22bold%20highlight-yellow%22%3Euser_main.py%3C/span%3E" STYLE="fork"/>
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
          <node TEXT="派送员登录" ID="VcVpcGB9hB" _mubu_text="%3Cspan%3E%E6%B4%BE%E9%80%81%E5%91%98%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
            <node TEXT="进入主界面" ID="XgZwF2tzwd" _mubu_text="%3Cspan%3E%E8%BF%9B%E5%85%A5%E4%B8%BB%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork">
              <node TEXT="deliverman.py" ID="fKn4Wynefg" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Edeliverman.py%3C/span%3E" STYLE="fork">
                <node TEXT="退出登陆" ID="ROyYTGvSSm" _mubu_text="%3Cspan%3E%E9%80%80%E5%87%BA%E7%99%BB%E9%99%86%3C/span%3E" STYLE="fork">
                  <node TEXT="回退到login.py" ID="stKo0WiyNM" _mubu_text="%3Cspan%3E%E5%9B%9E%E9%80%80%E5%88%B0%3C/span%3E%3Cspan%20class=%22bold%20highlight-yellow%22%3Elogin.py%3C/span%3E" STYLE="fork"/>
                </node>
                <node TEXT="选择最新到达位置" ID="MYM4LjP2Ru" _mubu_text="%3Cspan%3E%E9%80%89%E6%8B%A9%E6%9C%80%E6%96%B0%E5%88%B0%E8%BE%BE%E4%BD%8D%E7%BD%AE%3C/span%3E" STYLE="fork">
                  <node TEXT="确认更改" ID="8rxtDoTcND" _mubu_text="%3Cspan%3E%E7%A1%AE%E8%AE%A4%E6%9B%B4%E6%94%B9%3C/span%3E" STYLE="fork">
                    <node TEXT="弹窗回馈更改与否" ID="Uyp7q7OBMt" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E5%9B%9E%E9%A6%88%E6%9B%B4%E6%94%B9%E4%B8%8E%E5%90%A6%3C/span%3E" STYLE="fork"/>
                  </node>
                </node>
              </node>
            </node>
          </node>
          <node TEXT="快递员登录" ID="5hIuz7c98w" _mubu_text="%3Cspan%3E%E5%BF%AB%E9%80%92%E5%91%98%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
            <node TEXT="进入主界面" ID="5tWW3ZYt0Z" _mubu_text="%3Cspan%3E%E8%BF%9B%E5%85%A5%E4%B8%BB%E7%95%8C%E9%9D%A2%3C/span%3E" STYLE="fork">
              <node TEXT="postman_main.py" ID="F76ZehzLb5" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Epostman_main.py%3C/span%3E" STYLE="fork">
                <node TEXT="查询订单" ID="k8F5reaZSk" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%E8%AE%A2%E5%8D%95%3C/span%3E" STYLE="fork">
                  <node TEXT="postman_search_delivery.py" ID="1qzMJZHC4t" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Epostman_search_delivery.py%3C/span%3E" STYLE="fork">
                    <node TEXT="返回上一级" ID="tVycg3Sdnr" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%E4%B8%8A%E4%B8%80%E7%BA%A7%3C/span%3E" STYLE="fork">
                      <node TEXT="返回postman_main.py" ID="FUAoeSMK2D" _mubu_text="%3Cspan%3E%E8%BF%94%E5%9B%9E%3C/span%3E%3Cspan%20class=%22bold%20highlight-yellow%22%3Epostman_main.py%3C/span%3E" STYLE="fork"/>
                    </node>
                    <node TEXT="输入快递单号" ID="4XuqS3Tr5q" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E5%BF%AB%E9%80%92%E5%8D%95%E5%8F%B7%3C/span%3E" STYLE="fork">
                      <node TEXT="查询" ID="HJqyfg7vIb" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%3C/span%3E" STYLE="fork"/>
                    </node>
                  </node>
                </node>
                <node TEXT="添加取件码" ID="dsIuhzJNlG" _mubu_text="%3Cspan%3E%E6%B7%BB%E5%8A%A0%E5%8F%96%E4%BB%B6%E7%A0%81%3C/span%3E" STYLE="fork">
                  <node TEXT="postman_code.py" ID="IotqzkfFmR" _mubu_text="%3Cspan%20class=%22bold%20text-color-green%22%3Epostman_code.py%3C/span%3E" STYLE="fork">
                    <node TEXT="输入取件码" ID="Q3nBVazebX" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E5%8F%96%E4%BB%B6%E7%A0%81%3C/span%3E" STYLE="fork">
                      <node TEXT="确认添加" ID="6SoXyTjKQK" _mubu_text="%3Cspan%3E%E7%A1%AE%E8%AE%A4%E6%B7%BB%E5%8A%A0%3C/span%3E" STYLE="fork">
                        <node TEXT="弹窗提示结果" ID="4jZNynVFVF" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E6%8F%90%E7%A4%BA%E7%BB%93%E6%9E%9C%3C/span%3E" STYLE="fork"/>
                      </node>
                      <node TEXT="取消添加" ID="7mn7qHW4ix" _mubu_text="%3Cspan%3E%E5%8F%96%E6%B6%88%E6%B7%BB%E5%8A%A0%3C/span%3E" STYLE="fork">
                        <node TEXT="弹窗提示结果" ID="pghDxmSlIP" _mubu_text="%3Cspan%3E%E5%BC%B9%E7%AA%97%E6%8F%90%E7%A4%BA%E7%BB%93%E6%9E%9C%3C/span%3E" STYLE="fork"/>
                      </node>
                    </node>
                  </node>
                </node>
                <node TEXT="退出登陆" ID="GV7qYHQM0M" _mubu_text="%3Cspan%3E%E9%80%80%E5%87%BA%E7%99%BB%E9%99%86%3C/span%3E" STYLE="fork">
                  <node TEXT="退回login.py" ID="jTtwayqetw" _mubu_text="%3Cspan%3E%E9%80%80%E5%9B%9E%3C/span%3E%3Cspan%20class=%22bold%20highlight-yellow%22%3Elogin.py%3C/span%3E" STYLE="fork"/>
                </node>
              </node>
            </node>
          </node>
          <node TEXT="管理员登录" ID="Y9Ynab2OUh" _mubu_text="%3Cspan%3E%E7%AE%A1%E7%90%86%E5%91%98%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
            <node TEXT="admin.py" ID="HfshBXbuP7" _mubu_text="%3Cspan%20class=%22bold%20highlight-yellow%22%3Eadmin.py%3C/span%3E" STYLE="fork">
              <node TEXT="退出登录" ID="aCKamDk4Nb" _mubu_text="%3Cspan%3E%E9%80%80%E5%87%BA%E7%99%BB%E5%BD%95%3C/span%3E" STYLE="fork">
                <node TEXT="退回login.py" ID="B01XoSYo9T" _mubu_text="%3Cspan%3E%E9%80%80%E5%9B%9Elogin.py%3C/span%3E" STYLE="fork"/>
              </node>
              <node TEXT="查询配送员信息" ID="8Xovy860m3" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%E9%85%8D%E9%80%81%E5%91%98%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                <node TEXT="admin_manage_deliveryman.py" ID="yckRLgl4Sc" _mubu_text="%3Cspan%3Eadmin_manage_deliveryman.py%3C/span%3E" STYLE="fork">
                  <node TEXT="查询" ID="AVKP84zXnv" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%3C/span%3E" STYLE="fork">
                    <node TEXT="输入即可" ID="4MPPGNDSYj" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E5%8D%B3%E5%8F%AF%3C/span%3E" STYLE="fork"/>
                  </node>
                  <node TEXT="新建" ID="qFq7OXlEPj" _mubu_text="%3Cspan%3E%E6%96%B0%E5%BB%BA%3C/span%3E" STYLE="fork">
                    <node TEXT="输入即可" ID="khafd0oh0a" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E5%8D%B3%E5%8F%AF%3C/span%3E" STYLE="fork"/>
                  </node>
                  <node TEXT="修改" ID="k0qBPyc5wQ" _mubu_text="%3Cspan%3E%E4%BF%AE%E6%94%B9%3C/span%3E" STYLE="fork">
                    <node TEXT="选中然后修改对应值" ID="EUTPl3tiD4" _mubu_text="%3Cspan%3E%E9%80%89%E4%B8%AD%E7%84%B6%E5%90%8E%E4%BF%AE%E6%94%B9%E5%AF%B9%E5%BA%94%E5%80%BC%3C/span%3E" STYLE="fork"/>
                  </node>
                  <node TEXT="删除" ID="l2Un27MHmS" _mubu_text="%3Cspan%3E%E5%88%A0%E9%99%A4%3C/span%3E" STYLE="fork">
                    <node TEXT="选择然后删除" ID="z2tbfRNnWC" _mubu_text="%3Cspan%3E%E9%80%89%E6%8B%A9%E7%84%B6%E5%90%8E%E5%88%A0%E9%99%A4%3C/span%3E" STYLE="fork"/>
                  </node>
                </node>
              </node>
              <node TEXT="查看所有配送员" ID="lIiD7kBbxc" _mubu_text="%3Cspan%3E%E6%9F%A5%E7%9C%8B%E6%89%80%E6%9C%89%E9%85%8D%E9%80%81%E5%91%98%3C/span%3E" STYLE="fork">
                <node TEXT="admin_search_deliveryman.py" ID="LXPyhLY6LH" _mubu_text="%3Cspan%3Eadmin_search_deliveryman.py%3C/span%3E" STYLE="fork">
                  <node TEXT="输入工号或电话号码" ID="PcRjNFDVcl" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E5%B7%A5%E5%8F%B7%E6%88%96%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%3C/span%3E" STYLE="fork">
                    <node TEXT="查询" ID="2nyfZOdRig" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%3C/span%3E" STYLE="fork"/>
                  </node>
                </node>
              </node>
              <node TEXT="查询快递员信息" ID="y2CzozJKKn" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%E5%BF%AB%E9%80%92%E5%91%98%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                <node TEXT="admin_manage_postman.py" ID="Z44FORHzWI" _mubu_text="%3Cspan%3Eadmin_manage_postman.py%3C/span%3E" STYLE="fork">
                  <node TEXT="和配送员同理" ID="32QQDcM2Bm" _mubu_text="%3Cspan%3E%E5%92%8C%E9%85%8D%E9%80%81%E5%91%98%E5%90%8C%E7%90%86%3C/span%3E" STYLE="fork"/>
                </node>
              </node>
              <node TEXT="查看所有快递员" ID="gjr02OQlGp" _mubu_text="%3Cspan%3E%E6%9F%A5%E7%9C%8B%E6%89%80%E6%9C%89%E5%BF%AB%E9%80%92%E5%91%98%3C/span%3E" STYLE="fork">
                <node TEXT="" ID="oAFkTQd16g" _mubu_text="" STYLE="fork">
                  <node TEXT="输入工号或者电话号码" ID="dT8eT5RMv7" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E5%B7%A5%E5%8F%B7%E6%88%96%E8%80%85%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%3C/span%3E" STYLE="fork">
                    <node TEXT="查询" ID="ffF7Qbpl3n" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%3C/span%3E" STYLE="fork"/>
                  </node>
                </node>
              </node>
              <node TEXT="查询快递信息" ID="3KmSTNIq2g" _mubu_text="%3Cspan%3E%E6%9F%A5%E8%AF%A2%E5%BF%AB%E9%80%92%E4%BF%A1%E6%81%AF%3C/span%3E" STYLE="fork">
                <node TEXT="admin_search_delivery.py" ID="5Zt7cwtRWU" _mubu_text="%3Cspan%3Eadmin_search_delivery.py%3C/span%3E" STYLE="fork">
                  <node TEXT="输入查询即可" ID="qJSJVd82x8" _mubu_text="%3Cspan%3E%E8%BE%93%E5%85%A5%E6%9F%A5%E8%AF%A2%E5%8D%B3%E5%8F%AF%3C/span%3E" STYLE="fork"/>
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
  </node>
</map>