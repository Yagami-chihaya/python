# -*- coding:utf-8 -*-
import wx,sys,traceback,wx.adv,wx.lib
import wx.lib.agw.floatspin as lib_fs
import wx.lib.agw.hyperlink as lib_hyperlink
import wx.lib.agw.gradientbutton as lib_gb
import wx.lib.buttons as lib_button

def 窗口_取窗口句柄(组件):
    '出错返回False,取wxpython组件的窗口句柄'
    try:
        return 组件.GetHandle()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取组件祖组件(组件):
    '出错返回False,取wxpython组件的上上层组件,[当前-父组件-祖组件]'
    try:
        return 组件.GetGrandParent()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_对齐(组件,方向=12):
    '出错返回False,默认居中,使组件在父组件内对齐,主窗口则在屏幕中间,1.左上 4/5.顶边 8/9.左边 12/13.居中'
    try:
        return 组件.Center(方向)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取桌面相对坐标(组件,x=0,y=0):
    '出错返回(0,0),返回相对于此组件的坐标转换为屏幕坐标,x,y为偏移位置,0为当前'
    try:
        return 组件.ClientToScreen(x,y)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_关闭(窗口,关闭=True):
    '出错返回False,用来关闭窗口'
    try:
        return 窗口.Close(关闭)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False


def 窗口_销毁(窗口):
    '出错返回False,备注写的这个方法不会立即销毁窗口,会等事件执行后才安全的销毁'
    try:
        return 窗口.Destroy()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_销毁所有子窗口(组件):
    '出错返回False,销毁窗口下所有的子窗口,组件'
    try:
        return 组件.DestroyChildren()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_销毁2(窗口):
    '官方解释：计划在不久的将来销毁该窗口,每当销毁可能发生得太早时（例如，当该窗口或其子级仍在事件队列中等待时），都应使用此方法'
    try:
        return 窗口.DestroyLater()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_禁用(组件):
    '出错返回False,组件禁用后连同子级组件也无法点击移动'
    try:
        return 组件.Disable()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_禁用2(组件):
    '出错返回False,启用或禁用用于用户输入的窗口'
    try:
        return 组件.Enable(False)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_允许拖放文件(组件,允许=True):
    '允许接收拖放文件'
    try:
        return 组件.DragAcceptFiles(允许)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_ID匹配组件(父窗口,id):
    '找不到,出错返回False,在父窗口下查找返回该ID的组件'
    try:
        return 父窗口.FindWindow(id)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_ID匹配组件2(父窗口,id):
    '找不到,出错返回False,在父窗口下查找返回匹配到的第一个该ID的组件,可使用wx.FindWindowById全程序查找'
    try:
        return 父窗口.FindWindowById(id)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取键盘焦点组件(父窗口):
    '找不到,出错返回False,在父窗口下查找当前具有键盘焦点的窗口或控件'
    try:
        return 父窗口.FindFocus()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_标题匹配组件(父窗口,标题):
    '找不到,出错返回False,通过组件标题查找返回匹配到的第一个组件,可使用wx.FindWindowByLabel全程序查找'
    try:
        return 父窗口.FindWindowByLabel(标题)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_名称匹配组件(父窗口,组件名):
    '找不到,出错返回False,通过组件标题查找返回匹配到的第一个组件,可使用wx.FindWindowByName全程序查找'
    try:
        return 父窗口.FindWindowByName(组件名)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_自动调整尺寸(组件):
    '出错返回False,调整窗口大小以适合其最佳大小。'
    try:
        return 组件.Fit()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_自动调整内部尺寸(组件):
    '出错返回False,与相似Fit，但是调整窗户的内部（虚拟）尺寸,主要用于滚动窗口，以在调整大小而不会触发大小事件的情况下重置滚动条，和/或不带内部大小调整器的滚动窗口。如果没有子窗口，此功能同样不会执行任何操作。'
    try:
        return 组件.FitInside()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_禁止重画(组件):
    '出错返回False,冻结窗口，换句话说，阻止任何更新在屏幕上发生，窗口根本不会重绘'
    try:
        return 组件.Freeze()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_允许重画(组件):
    '出错返回False,重新启用窗口更新'
    try:
        return 组件.Thaw()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取背景颜色(组件):
    '出错返回False,返回窗口的背景色,格式:(240, 240, 240, 255)'
    try:
        return 组件.GetBackgroundColour()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取样式(组件):
    '出错返回False,样式：0.默认背景样式值,1.使用由系统或当前主题确定的默认背景,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.无介绍,4.表示未擦除窗口背景，从而使父窗口得以显示'
    try:
        return 组件.GetBackgroundStyle()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取最小可接受尺寸(组件):
    '出错返回False,回窗口的最佳可接受最小尺寸,返回格式:(宽度,高度)，高度不包含标题栏高度'
    try:
        return 组件.GetBestSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取最大可接受尺寸(组件):
    '出错返回False,回窗口的最佳可接受最小尺寸,返回格式:(宽度,高度)，高度不包含标题栏高度'
    try:
        return 组件.GetBestVirtualSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取边框样式(组件):
    '出错返回False,获取此窗口的标志的边框'
    try:
        return 组件.GetBorder()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取额外样式(组件):
    '出错返回False,窗口的额外样式位'
    try:
        return 组件.GetExtraStyle()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取字体高度(组件):
    '出错返回False,返回此窗口的字符高度'
    try:
        return 组件.GetCharHeight()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取平均字符宽度(组件):
    '出错返回False,返回此窗口的平均字符宽度'
    try:
        return 组件.GetCharWidth()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_遍历下级组件(组件):
    '出错返回False,遍历组件下的子级组件,返回在WindowList 列表里'
    try:
        return 组件.GetChildren()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取字体及颜色(组件):
    '出错返回False,返回字体,背景颜色,前景颜色，#(<wx._core.Font object at 0x000002140997DB88>, wx.Colour(240, 240, 240, 255), wx.Colour(0, 0, 0, 255))'
    try:
        结果 = 组件.GetClassDefaultAttributes()
        return 结果.font,结果.colBg,结果.colFg
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取矩形(组件):
    '出错返回False,返回窗口矩形：(左边,顶边,宽度,高度)'
    try:
        return 组件.GetRect()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取矩形2(组件):
    '出错返回False,返回窗口矩形：(0,0,宽度,高度)'
    try:
        return 组件.GetClientRect()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取宽高(组件):
    '出错返回False,返回窗口实际宽高：(宽度,高度)'
    try:
        return 组件.GetClientSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取宽高2(组件):
    '出错返回False,将窗口的最佳大小合并为最小大小，然后返回结果,返回宽高：(宽度,高度)'
    try:
        return 组件.GetEffectiveMinSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取字体(组件):
    '出错返回False,返回此窗口的字体'
    try:
        return 组件.GetFont()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取前景色(组件):
    '出错返回False,返回窗口的前景色'
    try:
        return 组件.GetForegroundColour()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取标记ID(组件):
    '出错返回False,返回窗口的标识符'
    try:
        return 组件.GetId()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取标题(组件):
    '出错返回False,返回窗口的标题'
    try:
        return 组件.GetLabel()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_置工作区宽高(组件,宽度,高度):
    '出错返回False,设置组件工作区的宽高(不包含边框,标题栏的宽高)'
    try:
        return 组件.SetClientSize(宽度,高度)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取工作区最小宽高(组件):
    '出错返回False,返回窗口的工作区的最小大小，这向sizer布局机制指示这是其工作区的最小所需大小'
    try:
        return 组件.GetMinClientSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取最小宽高(组件):
    '出错返回False,返回窗口的最小大小，这向sizer布局机制指示这是最小所需大小'
    try:
        return 组件.GetMinSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取组件名称(组件):
    '出错返回False,返回窗口的名称'
    try:
        return 组件.GetName()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取下一窗口(组件):
    '出错返回False,返回此窗口之后的下一个窗口(同一级窗口里)'
    try:
        return 组件.GetNextSibling()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取上一窗口(组件):
    '出错返回False,返回父级的子级中前一个的前一个窗口'
    try:
        return 组件.GetPrevSibling()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取父级窗口(组件):
    '出错返回False,返回窗口的父级，或者返回没有父级的窗口None'
    try:
        return 组件.GetParent()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

#未测试
def 窗口_弹出菜单(组件,菜单,左边,顶边):
    '出错返回False,此函数在此窗口中的给定位置显示一个弹出菜单，并返回所选的ID'
    try:
        return 组件.GetPopupMenuSelectionFromUser(菜单,左边,顶边)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取左边顶边(组件):
    '出错返回False,这将获得相对于子窗口的父窗口或相对于顶级窗口的显示原点的窗口位置（以像素为单位）,格式：(左边,顶边)'
    try:
        return 组件.DirDialog()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取窗口相对屏幕坐标(组件):
    '出错返回False,返回窗口在屏幕坐标中的位置，无论该窗口是子窗口还是顶级窗口,格式:(相对于屏幕的左边,相对于屏幕的顶边)'
    try:
        return 组件.GetScreenPosition()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取窗口相对屏幕矩形(组件):
    '出错返回False,返回窗口在屏幕坐标中的位置，无论该窗口是子窗口还是顶级窗口,格式:(相对于屏幕的左边,相对于屏幕的顶边,组件宽度,组件高度)'
    try:
        return 组件.GetScreenRect()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取内置滚动条位置(组件,方向):
    '出错返回False,返回内置滚动条的位置,方向：4.横向滚动条 8.纵向滚动条'
    try:
        return 组件.GetScrollPos(方向)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取内置滚动条范围(组件,方向):
    '出错返回False,返回内置滚动条范围,方向：4.横向滚动条 8.纵向滚动条'
    try:
        return 组件.GetScrollRange(方向)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取内置滚动条缩略图大小(组件,方向):
    '出错返回False,返回内置滚动条的缩略图大小,方向：4.横向滚动条 8.纵向滚动条'
    try:
        return 组件.GetScrollThumb(方向)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_置滚动条位置(组件,方向,位置,重绘):
    '出错返回False,设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)'
    try:
        return 组件.SetScrollPos(方向,位置,重绘)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_置滚动条属性(组件,方向,位置,可见大小,最大位置,重绘):
    '''
    出错返回False,设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)
    假设您希望使用相同的字体显示50行文本。窗口的大小设置为一次只能看到16行。您将使用：
    self.SetScrollbar(wx.VERTICAL, 0, 16, 50)
    '''
    try:
        return 组件.SetScrollbar(方向,位置,可见大小,最大位置,重绘)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取完整窗口宽高(组件):
    '出错返回False,返回整个窗口的大小（以像素为单位），包括标题栏，边框，滚动条等。如果此窗口是顶级窗口，并且当前已最小化，则返回的大小是还原的窗口大小，而不是窗口图标的大小'
    try:
        return 组件.GetSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否使用系统主题设置背景(组件):
    '出错返回False,窗口是否使用系统主题绘制其背景'
    try:
        return 组件.GetThemeEnabled()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取顶级窗口(组件):
    '出错返回False,返回此窗口（顶级窗口）的第一个祖先'
    try:
        return 组件.GetTopLevelParent()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_取虚拟宽高(组件):
    '出错返回False,这将获取窗口的虚拟大小,它返回窗口的客户端大小，但是在调用SetVirtualSize 它之后，将返回使用该方法设置的大小'
    try:
        return 组件.GetVirtualSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否有焦点(组件):
    '出错返回False,窗口（或在复合控件的情况下，其主子窗口）是否具有焦点'
    try:
        return 组件.HasFocus()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否有滚动条(组件,方向):
    '出错返回False,返回此窗口当前是否具有该方向的滚动条,方向：4.横向滚动条 8.纵向滚动条'
    try:
        return 组件.HasScrollbar(方向)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否透明(组件):
    '出错返回False,返回此窗口背景是否透明（例如，对于 wx.StaticText），并应显示父窗口背景'
    try:
        return 组件.HasTransparentBackground()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_隐藏(组件):
    '出错返回False,此功能可隐藏一个窗口'
    try:
        return 组件.Hide()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_隐藏带特效(组件,效果,效果时长):
    '''
    出错返回False,此功能可隐藏一个窗口并使用特殊的视觉效果
    效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
    效果时长：单位毫秒
    '''
    try:
        return 组件.HideWithEffect(效果,效果时长)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_显示带特效(组件,效果,效果时长):
    '''
    出错返回False,此功能可隐藏一个窗口并使用特殊的视觉效果
    效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
    效果时长：单位毫秒
    '''
    try:
        return 组件.ShowWithEffect(效果,效果时长)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False


def 窗口_是否继承父级背景色(组件):
    '出错返回False,如果此窗口从其父级继承背景色，则返回True'
    try:
        return 组件.InheritsBackgroundColour()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False


def 窗口_是否继承父级前景色(组件):
    '出错返回False,如果此窗口从其父级继承前景色，则返回True'
    try:
        return 组件.InheritsForegroundColour()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_重置缓存最佳大小(组件):
    '出错返回False,重置缓存的最佳大小值，以便下次需要时重新计算'
    try:
        return 组件.InvalidateBestSize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否正在销毁(组件):
    '出错返回False,此窗口是否正在销毁中'
    try:
        return 组件.IsBeingDeleted()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否为下级窗口(组件,对比组件):
    '出错返回False,检查指定的窗口是否是该窗口的后代,窗口是否为该窗口的后代（例如，子代或孙代或子孙或……）返回True'
    try:
        return 组件.IsDescendant(对比组件)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name,traceback.format_exc()))
        return False

def 窗口_是否禁用(组件):
    '出错返回False,是否启用了窗口，即是否接受用户输入'
    try:
        return 组件.IsEnabled()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否可获取焦点(组件):
    '出错返回False,判断窗口是否可以获取焦点'
    try:
        return 组件.IsFocusable()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否禁止重画(组件):
    '出错返回False,判断窗口是否可已经禁止重画'
    try:
        return 组件.IsFrozen()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否始终显示滚动条(组件,方向):
    '出错返回False,判断滚动条是否始终显示,方向：4.横向滚动条 8.纵向滚动条'
    try:
        return 组件.IsScrollbarAlwaysShown(方向)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否隐藏(组件):
    '出错返回False,判断是否调用命令隐藏了窗口,最小化,遮挡,不算隐藏'
    try:
        return 组件.IsShown()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否显示在屏幕上(组件):
    '出错返回False,判断是否调用命令隐藏了窗口,最小化,遮挡,不算隐藏'
    try:
        return 组件.IsShownOnScreen()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否启用(组件):
    '出错返回False,是否从本质上启用了此窗口，False否则返回'
    try:
        return 组件.IsThisEnabled()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否为顶级窗口(组件):
    '出错返回False,窗口是否为顶级窗口'
    try:
        return 组件.IsTopLevel()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_向下滚动(组件):
    '出错返回False,与ScrollLines （1）相同，返回True是否滚动窗口，False如果窗口已经在底部，则什么也不做'
    try:
        return 组件.LineDown()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_向上滚动(组件):
    '出错返回False,与ScrollLines （-1）相同,返回True是否滚动窗口，False如果窗口已经在顶部，则什么也不做'
    try:
        return 组件.LineUp()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_滚动_页(组件,滚动页数=1):
    '出错返回False,滚动页数:向上滚动1次为-1,向下为1'
    try:
        return 组件.ScrollPages(滚动页数)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_滚动_行(组件,滚动行数=1):
    '出错返回False,滚动行数:向上滚动1次为-1,向下为1'
    try:
        return 组件.ScrollLines(滚动行数)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_移动左边顶边(组件,左边,顶边):
    '出错返回False,调整移动窗口的左边跟顶边位置'
    try:
        return 组件.Move(左边,顶边)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_移动左边顶边2(组件,左边,顶边):
    '出错返回False,调整移动窗口的左边跟顶边位置'
    try:
        return 组件.SetPosition((左边,顶边))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_移动(组件,左边=-1,顶边=-1,宽度=-1,高度=-1):
    '出错返回False,调整移动窗口的左边跟顶边位置并重新设置宽度跟高度,不想调整的填-1'
    try:
        return 组件.SetSize(左边,顶边,宽度,高度)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_设置切换顺序_上(组件,上一个组件):
    '出错返回False,调整TAB切换的顺序,当上一个组件按TAB后焦点就会到当前组件上'
    try:
        return 组件.MoveAfterInTabOrder(上一个组件)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_设置切换顺序_下(组件,下一个组件):
    '出错返回False,调整TAB切换的顺序,当前组件按TAB后焦点会切换到下一个组件'
    try:
        return 组件.MoveBeforeInTabOrder(下一个组件)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_生成组件ID(组件):
    '出错返回False,创建一个新的ID或当前未使用的ID范围,格式:-31987'
    try:
        return 组件.NewControlId()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_重绘指定区域(组件,矩形=(0,0,0,0),擦除背景=True):
    '出错返回False,重绘指定矩形的内容：仅对其内部的区域进行重绘'
    try:
        return 组件.RefreshRect(矩形,擦除背景)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_修改父级窗口(组件,新父级组件):
    '出错返回False,即该窗口将从其当前父窗口中移除加入到新的父级窗口下'
    try:
        return 组件.Reparent(新父级组件)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_桌面坐标转窗口内坐标(组件,x,y):
    '出错返回False,从屏幕转换为客户端窗口内工作区坐标,'
    try:
        return 组件.ScreenToClient(x,y)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_到最顶层(组件):
    '出错返回False'
    try:
        return 组件.Raise()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_到最底层(组件):
    '出错返回False'
    try:
        return 组件.Lower()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否已设置背景色(组件):
    '出错返回False'
    try:
        return 组件.UseBackgroundColour()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否已设置前景色(组件):
    '出错返回False'
    try:
        return 组件.UseForegroundColour()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置背景颜色(组件,颜色):
    '出错返回False,设置背景颜色'
    try:
        return 组件.SetBackgroundColour(颜色)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_单独置背景颜色(组件,颜色):
    '出错返回False,设置窗口的背景色，但防止其被该窗口的子级继承'
    try:
        return 组件.SetOwnBackgroundColour(颜色)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置前景颜色(组件,颜色):
    '出错返回False,设置前景颜色'
    try:
        return 组件.SetForegroundColour(颜色)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_单独置前景颜色(组件,颜色):
    '出错返回False,设置窗口的前景色，但防止其被该窗口的子代继承'
    try:
        return 组件.SetOwnForegroundColour(颜色)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置标识ID(组件,ID):
    '出错返回False,设置表示ID'
    try:
        return 组件.SetId(ID)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置宽高(组件,宽度,高度):
    '出错返回False'
    try:
        return 组件.SetInitialSize((宽度,高度))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置最大宽高(组件,宽度,高度):
    '出错返回False,设置整个窗口最大尺寸范围'
    try:
        return 组件.SetMaxSize((宽度,高度))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置最小宽高(组件,宽度,高度):
    '出错返回False,设置整个窗口最大尺寸范围'
    try:
        return 组件.SetMinSize((宽度,高度))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置工作区最大宽高(组件,宽度,高度):
    '出错返回False,设置窗口的最大客户端大小(不包含标题栏菜单栏状态栏的尺寸)，以向sizer布局机制指示这是其客户端区域的最大可能大小'
    try:
        return 组件.SetMaxClientSize((宽度,高度))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置工作区最小宽高(组件,宽度,高度):
    '出错返回False,设置窗口的最大客户端大小(不包含标题栏菜单栏状态栏的尺寸)，以向sizer布局机制指示这是其客户端区域的最大可能大小'
    try:
        return 组件.SetMinClientSize((宽度,高度))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置虚拟宽高(组件,宽度,高度):
    '出错返回False,设置窗口的虚拟大小（以像素为单位）'
    try:
        return 组件.SetVirtualSize((宽度,高度))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置标题(组件,标题):
    '出错返回False,设置标题'
    try:
        return 组件.SetLabel(标题)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置名称(组件,名称):
    '出错返回False,设置名称'
    try:
        return 组件.SetName(名称)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_是否允许透明(组件):
    '出错返回False,判断组件是否允许设置透明度'
    try:
        return 组件.CanSetTransparent()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False


def 窗口_置透明度(组件,透明度):
    '出错返回False,设置窗口与透明度,范围0-255(0.完全透明,255完全不透明)'
    try:
        return 组件.SetTransparent(透明度)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置主题样式(组件,样式):
    '出错返回False,窗口样式:0.默认(可擦除背景),1.跟随系统主题,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.表示未擦除窗口背景，从而使父窗口得以显示,4.无描述。'
    try:
        return 组件.SetBackgroundStyle(样式)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置窗口样式(组件,样式):
    '出错返回False，样式:0.无边框,536870912.右上角无按钮,更多样式百度'
    try:
        return 组件.SetWindowStyleFlag(样式)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_刷新重绘(组件,删除背景=False):
    '出错返回False,导致GTK1重新绘制此窗口及其所有子级（除非未实现此子级）'
    try:
        return 组件.Refresh(删除背景)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_刷新重绘2(组件):
    '出错返回False,调用此方法将立即重新绘制窗口的无效区域及其所有子级的对象（通常仅在控制流返回事件循环时才发生）'
    try:
        return 组件.Update()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_显示或隐藏(组件,是否显示=True):
    '出错返回False,显示或隐藏窗口'
    try:
        return 组件.Show(是否显示)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_移动鼠标(组件,x,y):
    '出错返回False,将指针移动到窗口上的指定位置'
    try:
        return 组件.WarpPointer(x,y)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_置鼠标光标样式(组件,样式):
    '''出错返回False,样式:
    0:无描述
    1:标准箭头光标。
    2:指向右侧的标准箭头光标。
    3:靶心光标。
    4:矩形字符光标。
    5:十字光标。
    6:手形光标。
    7:工字梁光标（垂直线）。
    8:表示鼠标左键按下。
    9:放大镜图标。
    10:表示按下中间按钮的鼠标。
    11:不可输入的符号光标。
    12:画笔光标。
    13:铅笔光标。
    14:指向左的光标。
    15:指向右的光标。
    16:箭头和问号。
    17:表示按下了右键的鼠标。
    18:调整大小的光标指向NE-SW。
    19:调整大小的光标指向N-S。
    20:调整大小的光标指向NW-SE。
    21:调整大小的光标指向W-E。
    22:一般大小的游标。
    23:Spraycan游标。
    24:等待光标。
    25:监视光标。
    26:透明光标。
    27:带有标准箭头的等待光标。
    28:无描述。
    '''
    try:
        return 组件.SetCursor(wx.Cursor(样式))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 窗口_设置字体(组件,字体名,大小,粗细,下划线):
    '出错返回False,窗口样式:0.默认(可擦除背景),1.跟随系统主题,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.表示未擦除窗口背景，从而使父窗口得以显示,4.无描述。'
    try:
        return 组件.SetFont(wx.Font(大小,wx.DEFAULT, wx.NORMAL, 粗细, 下划线, 字体名))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False








def 程序_取指定坐标处组件(x,y):
    '出错返回None,传入桌面上坐标'
    try:
        return wx.FindWindowAtPoint((x,y))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return None

def 程序_取鼠标处组件跟坐标():
    '出错返回None,取当前鼠标下面的组件及坐标,返回格式:(组件,(x,y)),返回的坐标是相对于桌面的坐标'
    try:
        return wx.FindWindowAtPointer()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return None

def 程序_取屏幕工作区矩形():
    '出错返回False,取屏幕工作区矩形(不包含任务栏宽高),格式：(0,0,1920,1040) 任务栏占了40'
    try:
        return wx.GetClientDisplayRect()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_取屏幕分辨率():
    '出错返回False,返回格式:(1920,1080)'
    try:
        return wx.GetDisplaySize()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_取屏幕尺寸():
    '出错返回False,返回以毫米为单位的显示尺寸，格式:(508,286)'
    try:
        return wx.GetDisplaySizeMM()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_恢复默认鼠标光标():
    '出错返回False,对于应用程序中的所有窗口，将光标更改回原始光标'
    try:
        return wx.EndBusyCursor()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_重置所有鼠标光标(光标类型):
    '''出错返回False,将光标更改为应用程序中所有窗口的给定光标
    光标类型:
    0:无描述
    1:标准箭头光标。
    2:指向右侧的标准箭头光标。
    3:靶心光标。
    4:矩形字符光标。
    5:十字光标。
    6:手形光标。
    7:工字梁光标（垂直线）。
    8:表示鼠标左键按下。
    9:放大镜图标。
    10:表示按下中间按钮的鼠标。
    11:不可输入的符号光标。
    12:画笔光标。
    13:铅笔光标。
    14:指向左的光标。
    15:指向右的光标。
    16:箭头和问号。
    17:表示按下了右键的鼠标。
    18:调整大小的光标指向NE-SW。
    19:调整大小的光标指向N-S。
    20:调整大小的光标指向NW-SE。
    21:调整大小的光标指向W-E。
    22:一般大小的游标。
    23:Spraycan游标。
    24:等待光标。
    25:监视光标。
    26:透明光标。
    27:带有标准箭头的等待光标。
    28:无描述。
    '''
    try:
        return wx.BeginBusyCursor(wx.Cursor(光标类型))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_关闭2():
    "立即结束程序"
    wx.Abort()

def 程序_关闭():
    "立即结束程序,会卡顿下"
    wx.Exit()

def 程序_系统错误代码转提示文本(code):
    "返回与给定系统错误代码对应的错误消息,示例：code=3 返回:系统找不到指定的路径。"
    try:
        return wx.SysErrorMsgStr(3)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_电脑关机():
    "立即结束程序,会卡顿下"
    wx.Shutdown(2)

def 程序_电脑重启():
    "立即结束程序,会卡顿下"
    wx.Shutdown(4)

def 程序_执行Shell(内容):
    "执行成功返回True否则False"
    try:
        wx.Shell(内容)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_延时_微秒(时间):
    "延时单位(微秒)1秒=1000000微秒"
    wx.MicroSleep(时间)

def 程序_延时_毫秒(时间):
    "延时单位(毫秒)1秒=1000毫秒"
    wx.MilliSleep(时间)

def 程序_延时_秒(时间):
    wx.Sleep(时间)

def 程序_取本地英文时间():
    "返回时间示例：Sun Aug 16 15:57:41 2020"
    wx.Now()

def 程序_取程序对象():
    "返回当前应用程序对象"
    return wx.GetApp()

def 程序_取程序顶级窗口列表():
    "返回应用程序顶级窗口的类似列表的对象(返回顶级窗口的对象列表)"
    return wx.GetTopLevelWindows()

def 程序_取计算机名():
    "返回当前应用程序对象"
    return wx.GetHostName()

def 程序_取系统版本信息():
    "返回示例: Windows 10 (build 18363)，64位版"
    return wx.GetOsDescription()

def 程序_取系统用户名():
    "返回示例: Administrator"
    return wx.GetUserName()

def 程序_系统是否64位():
    "返回True程序运行所在的操作系统是否为64位。"
    return wx.IsPlatform64Bit()

def 程序_打开指定网址或目录(地址):
    "可以打开电脑目录或使用默认浏览器打开指定网址"
    try:
        return wx.LaunchDefaultBrowser(地址)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_打开指定网址(url):
    try:
        import webbrowser
        return webbrowser.open(url)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 程序_取鼠标坐标():
    "返回鼠标坐标(x,y)"
    return wx.GetMouseState().GetPosition()

def 程序_鼠标侧键1是否按下():
    "返回当前应用程序对象,判断鼠标侧边附加的按键是否按下"
    return wx.GetMouseState().Aux1IsDown()

def 程序_鼠标侧键2是否按下():
    "返回True或False,判断鼠标侧边附加的按键是否按下"
    return wx.GetMouseState().Aux2IsDown()

def 程序_鼠标左键是否按下():
    "返回True或False,判断鼠标左键是否按下"
    return wx.GetMouseState().LeftIsDown()

def 程序_鼠标中键是否按下():
    "返回True或False,判断鼠标中键是否按下"
    return wx.GetMouseState().MiddleIsDown()

def 程序_鼠标右键是否按下():
    "返回True或False,判断鼠标右键是否按下"
    return wx.GetMouseState().RightIsDown()

def 程序_取当前进程ID():
    "返回当前程序进程PID"
    return wx.GetProcessId()

def 程序_系统环境是否支持中文():
    "返回True或False    更多环境语言方法参考:https://wxpython.org/Phoenix/docs/html/wx.Language.enumeration.html#wx-language"
    return wx.GetLocale().IsAvailable(wx.LANGUAGE_CHINESE)

def 程序_取环境语言名称():
    "返回示例: Chinese (Simplified)    更多环境语言方法参考:https://wxpython.org/Phoenix/docs/html/wx.Locale.html#wx-locale"
    return wx.GetLocale().GetLocale()

def 程序_取环境语言缩写():
    "返回实力: zh_CN    更多环境语言方法参考:https://wxpython.org/Phoenix/docs/html/wx.Locale.html#wx-locale"
    return wx.GetLocale().GetName()

def 程序_系统是否已激活():
    "返回True或False,不太确定是不是这个命令,获取更多电脑描述信息参考:https://wxpython.org/Phoenix/docs/html/wx.VersionInfo.html#wx-versioninfo"
    return wx.GetLibraryVersionInfo().HasCopyright()















def 组件_信息框(标题="信息",提示="",类型=0,父窗口=None):
    """
    类型:
    0.无图标信息框
    1.带取消键普通信息框
    2.带是/否键普通信息框
    3.带帮助键普通信息框
    4.带红色错误图标信息框
    5.带黄色感叹标题信息框
    6.带盾牌(类似权限验证)图标信息框

    返回值:2.是   4.确定   8.否   16.取消/关闭   4096.帮助
    """
    字典 = {0:262144,1:16,2:10,3:4096,4:512,5:256,6:524288}
    try:
        return wx.MessageBox(提示,标题,字典[类型],父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return 16


def 组件_提示信息框(内容):
    "出错返回False,弹出一个带蓝色反向感叹号图标的信息框"
    try:
        return wx.LogMessage(内容)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 组件_警告信息框(内容):
    "出错返回False,弹出一个带黄色三角形感叹号图标的信息框"
    try:
        return wx.LogWarning(内容)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 组件_报错信息框(内容):
    "出错返回False,弹出一个带红叉图标的信息框"
    try:
        return wx.LogError(内容)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False


def 组件_文件选择器(标题="请选择文件",初始路径="",默认文件名="",过滤器="所有文件|*.*",父窗口=None):
    "选择文件后返回完整文件路径,没选择返回空文本,可添加参数,flags(标识),parent(父窗口),x,y"
    try:
        return wx.FileSelector(标题, 初始路径,默认文件名, wildcard=过滤器)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_保存文件对话框(提示="",后缀="*",默认文件名="",父窗口=None):
    "设置文件后返回完整文件路径,没选择返回空文本"
    try:
        return wx.SaveFileSelector(提示, 后缀,默认文件名, 父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_目录选择器(提示="",初始路径="",父窗口=None):
    "选择目录后返回完整路径,没选择返回空文本,返回示例:c:\\user"
    try:
        return wx.DirSelector(message=提示, default_path=初始路径,parent=父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_颜色选择器(初始颜色=None,标题="请选择颜色",父窗口=None):
    "选择颜色后返回颜色值(0,0,0,255),没选择返回(-1, -1, -1, 255),可添加参数,flags(标识),parent(父窗口),x,y"
    try:
        return wx.GetColourFromUser(父窗口, 初始颜色,标题)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return (-1, -1, -1, 255)

def 组件_字体选择器(父窗口,默认字体=None,标题="请选择字体"):
    "选择字体后返回字体类型"
    try:
        return wx.GetFontFromUser(父窗口,默认字体 if 默认字体 else 父窗口.GetFont(),标题)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return False

def 组件_数值对话框(标题="请设置数值",提示="",参数提示="",默认值=1,最小值=1,最大值=100,父窗口=None):
    "不能在线程里调用,取消返回-1,弹出一个设置数值的对话框"
    try:
        return wx.GetNumberFromUser(提示, 参数提示, 标题, 默认值, 最小值, 最大值, 父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return -1

def 组件_密码对话框(提示="",标题="请输入密码",默认文本="",父窗口=None):
    "弹出一个文本对话框,输入的内容会被替换成圆点,适合密码等输入使用,确认后返回输入的内容,取消返回空文本"
    try:
        return wx.GetPasswordFromUser(message=提示,caption=标题, default_value=默认文本,parent=父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_单选列表对话框(提示="",标题="请选择",选择项=['未设置'],初始选中=0,父窗口=None):
    "弹出一个单选列表对话框,选择后返回选中的文本内容,取消返回空,选择项必须是文本型列表,初始选中从0开始"
    try:
        return wx.GetSingleChoice(message=提示,caption=标题,choices=选择项,initialSelection=初始选中,parent=父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_普通对话框(提示="",标题="请输入",默认文本='',父窗口=None):
    "弹出一个对话框输入文本,确认后返回输入的文本,取消返回空"
    try:
        return wx.GetTextFromUser(message=提示,caption=标题,default_value=默认文本,parent=父窗口)
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_气泡提示框(父窗口,提示="",标题="",超时时间=3000,x=0,y=0):
    "弹出一个气泡提示框,默认在组件中间,可通过设置x,y调整"
    try:
        气泡 = wx.adv.RichToolTip(标题,提示)
        气泡.SetTimeout(超时时间)
        气泡.ShowFor(父窗口,(0,0,x*2,y*2))
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''

def 组件_系统弹窗(父窗口=None,提示="",标题=""):
    "电脑右下角弹出一个提示框,可以绑定提示框点击事件,详细操作：https://wxpython.org/Phoenix/docs/html/wx.adv.NotificationMessage.html#wx.adv.NotificationMessage.Show"
    try:
        提示框 = wx.adv.NotificationMessage(标题,提示,父窗口)
        提示框.Show()
    except:
        print("{}|运行出错\r\n{}\r\n".format(sys._getframe().f_code.co_name, traceback.format_exc()))
        return ''







class class_ec():
    def 取窗口句柄(self):
        return self.GetHandle()

    def 取组件名称(self):
        return self.GetName()

    def 取标记ID(self):
        return self.GetId()

    def 取左边顶边(self):
        return self.GetPosition()

    def 取左边(self):
        return self.GetPosition()[0]

    def 取顶边(self):
        return self.GetPosition()[1]

    def 取宽度高度(self):
        return self.GetSize()

    def 取宽度高度2(self):
        return self.GetClientSize()

    def 取宽高3(self):
        '将窗口的最佳大小合并为最小大小'
        return self.GetEffectiveMinSize()

    def 取宽度(self):
        return self.GetSize()[0]

    def 取高度(self):
        return self.GetSize()[1]

    def 取祖组件(self):
        return self.GetGrandParent()

    def 取桌面相对坐标(self):
        "取组件左边跟顶边相对于桌面的坐标位置"
        return self.GetScreenPosition()

    def 取桌面相对坐标2(self):
        "取组件左边跟顶边相对于桌面的坐标位置"
        return self.ClientToScreen(0, 0)

    def 取窗口相对屏幕矩形(self):
        '出错返回False,返回窗口在屏幕坐标中的位置，无论该窗口是子窗口还是顶级窗口,格式:(相对于屏幕的左边,相对于屏幕的顶边,组件宽度,组件高度)'
        return self.GetScreenRect()

    def 取背景颜色(self):
        '返回窗口的背景色,格式:(240, 240, 240, 255)'
        return self.GetBackgroundColour()

    def 取可设置的最小尺寸(self):
        '返回窗口的最佳可接受最小尺寸, 返回格式: (宽度, 高度)，高度不包含标题栏高度'
        return self.GetBestSize()

    def 取可设置的最大尺寸(self):
        '返回窗口的最佳可接受最大尺寸, 返回格式: (宽度, 高度)，高度不包含标题栏高度'
        return self.GetBestVirtualSize()

    def 取主题样式(self):
        '样式：0.默认背景样式值,1.使用由系统或当前主题确定的默认背景,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.无介绍,4.表示未擦除窗口背景，从而使父窗口得以显示'
        return self.GetBackgroundStyle()

    def 取边框样式(self):
        return self.GetBorder()

    def 取额外样式(self):
        return self.GetExtraStyle()

    def 取字体及颜色(self):
        '返回: 字体,背景颜色,前景颜色，#(<wx._core.Font object at 0x000002140997DB88>, wx.Colour(240, 240, 240, 255), wx.Colour(0, 0, 0, 255))'
        结果 = self.GetClassDefaultAttributes()
        return 结果.font,结果.colBg,结果.colFg

    def 取矩形(self):
        '返回窗口矩形：(左边,顶边,宽度,高度)'
        return self.GetRect()

    def 取工作区矩形(self):
        return self.GetClientRect()

    def 取字体(self):
        return self.GetFont()

    def 取字体高度(self):
        '返回此窗口的字符高度'
        return self.GetCharHeight()

    def 取字体平均宽度(self):
        '返回此窗口的平均字符宽度'
        return self.GetCharWidth()

    def 取前景色(self):
        return self.GetForegroundColour()

    def 取标题(self):
        return self.GetLabel()

    def 取标题T(self):
        return self.GetTitle()

    def 取内容(self):
        return self.GetValue()

    def 取工作区最小宽高(self):
        '返回窗口的工作区的最小大小，这向sizer布局机制指示这是其工作区的最小所需大小'
        return self.GetMinClientSize()

    def 取最小宽高(self):
        '返回窗口的最小大小，这向sizer布局机制指示这是最小所需大小'
        return self.GetMinSize()

    def 取下一个组件(self):
        '返回下一个组件的对象，即按TAB键切换到的下一个组件'
        return self.GetNextSibling()

    def 取下上一个组件(self):
        '返回上一个组件的对象，即按TAB键切换到的上一个组件'
        return self.GetPrevSibling()

    def 取父窗口(self):
        '返回父窗口对象'
        return self.GetParent()

    def 取顶级窗口(self):
        return self.GetTopLevelParent()

    def 取虚拟宽高(self):
        '这将获取窗口的虚拟大小,它返回窗口的客户端大小，但是在调用SetVirtualSize 它之后，将返回使用该方法设置的大小'
        return self.GetVirtualSize()

    def 取内置滚动条缩略图大小(self,方向):
        '返回内置滚动条的缩略图大小,方向：4.横向滚动条 8.纵向滚动条'
        return self.GetScrollThumb(方向)

    def 取内置滚动条范围(self,方向):
        '返回内置滚动条范围,方向：4.横向滚动条 8.纵向滚动条'
        return self.GetScrollRange(方向)

    def 取内置滚动条位置(self, 方向):
        '返回内置滚动条的位置,方向：4.横向滚动条 8.纵向滚动条'
        return self.GetScrollPos(方向)





    def 置组件名称(self):
        return self.SetName()

    def 置标记ID(self):
        return self.SetId()

    def 置左边顶边(self,左边,顶边):
        return self.Move(左边,顶边)

    def 置左边顶边2(self,左边,顶边):
        return self.SetPosition(左边,顶边)

    def 置左边(self,左边):
        return self.Move(左边,self.GetPosition()[1])

    def 置顶边(self,顶边):
        return self.Move(self.GetPosition()[0],顶边)

    def 置左边2(self,左边):
        return self.SetPosition(左边,self.GetPosition()[1])

    def 置顶边2(self,顶边):
        return self.SetPosition(self.GetPosition()[0],顶边)

    def 置宽度高度(self,宽度,高度):
        return self.GetSize((宽度,高度))

    def 置宽度高度2(self,宽度,高度):
        return self.SetInitialSize((宽度,高度))

    def 置宽度(self,宽度):
        return self.SetInitialSize((宽度,self.GetSize()[1]))

    def 置高度(self,高度):
        return self.SetInitialSize((self.GetSize()[0],高度))

    def 置标题(self,标题):
        return self.SetLabel(标题)

    def 置标题T(self,标题):
        return self.SetTitle(标题)

    def 置内容(self,内容):
        return self.SetValue()

    def 置拖放权限(self,拖放=True):
        "设置是否允许接收拖放文件"
        return self.DragAcceptFiles(拖放)

    def 置工作区宽高(self, 宽度, 高度):
        '出设置组件工作区的宽高(不包含边框,标题栏的宽高)'
        return self.SetClientSize(宽度, 高度)

    def 置背景颜色(self,颜色):
        return self.SetBackgroundColour(颜色)

    def 单独置背景颜色(self,颜色):
        '设置窗口的背景色，但防止其被该窗口的子级继承'
        return self.SetOwnBackgroundColour(颜色)

    def 置前景颜色(self,颜色):
        return self.SetForegroundColour(颜色)

    def 单独置前景颜色(self,颜色):
        '设置窗口的前景色，但防止其被该窗口的子级继承'
        return self.SetOwnForegroundColour(颜色)

    def 置最大宽高(self,宽度,高度):
        '设置整个窗口最大可设置的尺寸'
        return self.SetMaxSize((宽度,高度))

    def 置最小宽高(self,宽度,高度):
        '设置整个窗口最小可设置的尺寸'
        return self.SetMinSize((宽度,高度))

    def 置工作区最大宽高(self,宽度,高度):
        '设置工作区最大可设置的尺寸'
        return self.SetMaxClientSize((宽度,高度))

    def 置工作区最小宽高(self,宽度,高度):
        '设置工作区最小可设置的尺寸'
        return self.SetMinClientSize((宽度,高度))

    def 置虚拟宽高(self,宽度,高度):
        '设置窗口的虚拟大小（以像素为单位）'
        return self.SetVirtualSize((宽度,高度))

    def 置透明度(self,透明度):
        '设置窗口与透明度,范围0-255(0.完全透明,255完全不透明)'
        return self.SetTransparent(透明度)

    def 置主题样式(self,样式):
        '窗口样式:0.默认(可擦除背景),1.跟随系统主题,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.表示未擦除窗口背景，从而使父窗口得以显示,4.无描述。'
        return self.SetBackgroundStyle(样式)

    def 置窗口样式(self,样式):
        return self.SetWindowStyleFlag(样式)

    def 置鼠标样式(self,样式):
        '''出错返回False,样式:
        0:无描述
        1:标准箭头光标。
        2:指向右侧的标准箭头光标。
        3:靶心光标。
        4:矩形字符光标。
        5:十字光标。
        6:手形光标。
        7:工字梁光标（垂直线）。
        8:表示鼠标左键按下。
        9:放大镜图标。
        10:表示按下中间按钮的鼠标。
        11:不可输入的符号光标。
        12:画笔光标。
        13:铅笔光标。
        14:指向左的光标。
        15:指向右的光标。
        16:箭头和问号。
        17:表示按下了右键的鼠标。
        18:调整大小的光标指向NE-SW。
        19:调整大小的光标指向N-S。
        20:调整大小的光标指向NW-SE。
        21:调整大小的光标指向W-E。
        22:一般大小的游标。
        23:Spraycan游标。
        24:等待光标。
        25:监视光标。
        26:透明光标。
        27:带有标准箭头的等待光标。
        28:无描述。
        '''
        return self.SetCursor(wx.Cursor(样式))

    def 置字体(self,字体):
        return self.SetFont(字体)

    def 置字体2(self,字体名,大小,粗细,下划线):
        return self.SetFont(wx.Font(大小,wx.DEFAULT, wx.NORMAL, 粗细, 下划线, 字体名))

    def 置文本颜色(self,颜色):
        return self.SetForegroundColour(颜色)

    def 置组件顺序_上(self,上一个组件):
        '设置使用TAB键切换组件时的切换顺序，从上一个组件按下TAB键后跳转到单前组件'
        return self.MoveAfterInTabOrder(上一个组件)

    def 置组件顺序_下(self,下一个组件):
        '设置使用TAB键切换组件时的切换顺序，从在单前组件按下TAB键后切换到下一个组件'
        return self.MoveBeforeInTabOrder(下一个组件)

    def 置滚动条属性(self,方向,位置,可见大小,最大位置,重绘):
        '''
        设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)
        假设您希望使用相同的字体显示50行文本。窗口的大小设置为一次只能看到16行。您将使用：
        self.SetScrollbar(wx.VERTICAL, 0, 16, 50)
        '''
        return self.SetScrollbar(方向,位置,可见大小,最大位置,重绘)

    def 置滚动条位置(self,方向,位置,重绘):
        '设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)'
        return self.SetScrollPos(方向,位置,重绘)


    def 销毁(self):
        return self.Destroy()

    def 销毁2(self):
        '官方解释：计划在不久的将来销毁该窗口,每当销毁可能发生得太早时（例如，当该窗口或其子级仍在事件队列中等待时），都应使用此方法'
        return self.DestroyLater()

    def 销毁子窗口(self):
        return self.DestroyChildren()

    def 禁用2(self):
        return self.Disable()

    def 禁用(self,禁用=True):
        "True为禁用组件，False为恢复组件使用"
        return self.Enable(not 禁用)

    def 禁止重画(self):
        return self.Freeze()

    def 允许重画(self):
        return self.Thaw()

    def 移动(self,左边=-1,顶边=-1,宽度=-1,高度=-1):
        '调整移动窗口的左边跟顶边位置并重新设置宽度跟高度,不想调整的填-1'
        return self.SetSize(左边,顶边,宽度,高度)

    def 刷新重绘(self,删除背景=False):
        '导致GTK1重新绘制此窗口及其所有子级（除非未实现此子级）'
        return self.Refresh(删除背景)

    def 刷新重绘2(self):
        '调用此方法将立即重新绘制窗口的无效区域及其所有子级的对象（通常仅在控制流返回事件循环时才发生）'
        return self.Update()

    def 遍历下级组件(self):
        '遍历组件下的子级组件,返回在WindowList 列表里'
        return self.GetChildren()

    def 弹出菜单(self, 菜单, 左边=0, 顶边=0):
        '此函数在此窗口中的给定位置显示一个弹出菜单，并返回所选的ID'
        return self.GetPopupMenuSelectionFromUser(菜单, 左边, 顶边)

    def 移动鼠标(self,x,y):
        '移动鼠标到组件内的指定位置'
        return self.WarpPointer(x,y)

    def 是否有焦点(self):
        return self.HasFocus()

    def 是否有滚动条(self,方向):
        '返回此窗口当前是否具有该方向的滚动条,方向：4.横向滚动条 8.纵向滚动条'
        return self.HasScrollbar(方向)

    def 是否透明(self):
        return self.HasTransparentBackground()

    def 显示或隐藏(self,是否显示=True):
        '显示或隐藏窗口'
        return self.Show(是否显示)

    def 隐藏(self):
        return self.Show(False)

    def 隐藏2(self):
        return self.Hide()

    def 隐藏_带特效(self,效果,效果时长):
        '''
        出错返回False,此功能可隐藏一个窗口并使用特殊的视觉效果
        效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
        效果时长：单位毫秒
        '''
        return self.HideWithEffect(效果, 效果时长)

    def 显示(self):
        return self.Show(True)

    def 显示_带特效(self, 效果, 效果时长):
        '''
        出错返回False,此功能可隐藏一个窗口并使用特殊的视觉效果
        效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
        效果时长：单位毫秒
        '''
        return self.ShowWithEffect(效果, 效果时长)

    def 是否继承父窗口背景色(self):
        return self.InheritsBackgroundColour()

    def 是否继承父窗口前景色(self):
        return self.InheritsForegroundColour()

    def 重置缓存最佳大小(self):
        '出错返回False,重置缓存的最佳大小值，以便下次需要时重新计算'
        return self.InvalidateBestSize()

    def 是否正在销毁(self):
        '出错返回False,此窗口是否正在销毁中'
        return self.IsBeingDeleted()

    def 是否禁用(self):
        return not self.IsEnabled()

    def 是否可获取焦点(self):
        return self.IsFocusable()

    def 是否为上级窗口(self,待判断组件):
        return self.IsDescendant(待判断组件)

    def 是否禁止重画(self):
        return self.IsFrozen()

    def 是否隐藏(self):
        '判断是否调用命令隐藏了窗口,最小化,遮挡,不算隐藏'
        return self.IsShown()

    def 是否允许透明(self):
        return self.CanSetTransparent()

    def 是否显示在屏幕上(self):
        return self.IsShownOnScreen()

    def 是否启用(self):
        '是否从本质上启用了此窗口，False否则返回'
        return self.IsThisEnabled()

    def 是否为顶级窗口(self):
        return self.IsTopLevel()

    def 重绘指定区域(self,矩形=(0,0,0,0),擦除背景=True):
        '重绘指定矩形的内容：仅对其内部的区域进行重绘'
        return self.RefreshRect(矩形, 擦除背景)

    def 修改父级窗口(self,新父级组件):
        '即该窗口将从其当前父窗口中移除加入到新的父级窗口下'
        return self.Reparent(新父级组件)

    def 桌面坐标转窗口内坐标(self,x,y):
        '从屏幕转换为客户端窗口内工作区坐标,'
        return self.ScreenToClient(x,y)

    def 到最顶层(self):
        '调整显示顺序'
        self.Raise()

    def 到最底层(self):
        '调整显示顺序'
        self.Lower()

    def 是否已设置背景色(self):
        return self.UseBackgroundColour()

    def 是否已设置前景色(self):
        return self.UseForegroundColour()

    def 向上滚动(self):
        '与ScrollLines （-1）相同,返回True是否滚动窗口，False如果窗口已经在顶部，则什么也不做'
        return self.LineUp()

    def 向下滚动(self):
        '与ScrollLines （1）相同，返回True是否滚动窗口，False如果窗口已经在底部，则什么也不做'
        return self.LineDown()

    def 是否始终显示滚动条(self,方向):
        '判断滚动条是否始终显示,方向：4.横向滚动条 8.纵向滚动条'
        return self.IsScrollbarAlwaysShown(方向)

    def 滚动_页(self,滚动页数=1):
        '滚动页数:向上滚动1次为-1,向下为1'
        return self.ScrollPages(滚动页数)

    def 滚动_行(self,滚动行数=1):
        '出错返回False,滚动行数:向上滚动1次为-1,向下为1'
        return self.ScrollLines(滚动行数)

    def 是否使用系统主题设置背景(self):
        '窗口是否使用系统主题绘制其背景'
        return self.GetThemeEnabled()


#窗口
class wx_Frame(wx.Frame,class_ec):

    def 关闭(self):
        self.Close(True)

    def 置图标(self,图标路径):
        icon = wx.Icon(图标路径)
        self.SetIcon(icon)

    def 居中(self):
        '将窗口调整到屏幕中间'
        self.Centre()

    def 创建状态栏(self,项目,抓取器=True):#只能创建一个
        "项目格式为list，每个成员为tuple 格式(项目名,宽度)，如[('项目1',-1),('项目2',-1)],负数表示按比例分配"
        try:
            if self.状态栏:
                return False
        except:
            pass

        样式 = wx.STB_SHOW_TIPS|wx.STB_ELLIPSIZE_END|wx.FULL_REPAINT_ON_RESIZE
        样式 += wx.STB_SIZEGRIP  if 抓取器 else 0
        self.状态栏 = self.CreateStatusBar(style=样式)
        self.状态栏.SetFieldsCount(len(项目))
        self.状态栏.SetStatusWidths([x[1] for x in 项目])
        for x in range(len(项目)):
            self.状态栏.SetStatusText(项目[x][0], x)

    def 置状态栏项目宽度(self,宽度列表):
        '需要传入一个整数列表设置全部项目宽度'
        self.状态栏.SetStatusWidths(宽度列表)

    def 置状态栏项目文本(self,索引,文本):
        self.状态栏.SetStatusText(文本, 索引)

    def 取状态栏项目数(self):
        return self.状态栏.GetFieldsCount()

    def 取状态栏项目文本(self,索引):
        return self.状态栏.GetStatusText(索引)

    def 取状态栏项目宽度(self,索引):
        return self.状态栏.GetStatusWidth(索引)

    def 取状态栏项目样式(self,索引):
        return self.状态栏.GetStatusStyle(索引)

    def 置状态栏最小宽度(self,宽度):
        return self.状态栏.SetMinHeight(宽度)

    def 置状态栏项目数(self,项目数,宽度列表=[]):
        宽度列表 = 宽度列表 if 宽度列表 else [-1 for x in range(项目数)]
        return self.状态栏.SetFieldsCount(项目数,宽度列表)


#按钮
class wx_Button(wx.Button,class_ec):

    def 置认证图标(self,显示=True):
        return self.SetAuthNeeded(显示)

    def 显示认证图标(self):
        return self.SetAuthNeeded()

    def 隐藏认证图标(self):
        return self.SetAuthNeeded(False)

    def 置顶层默认项(self):
        '设置后再窗口中按回车即可触发按钮点击事件'
        return self.SetDefault()


#标签
class wx_StaticText(wx.StaticText,class_ec):
    pass


#编辑框
class wx_TextCtrl(wx.TextCtrl,class_ec):

    def 取新文本样式(self):
        '返回当前用于新文本的样式。'
        return self.GetDefaultStyle()

    def 取指定行长度(self,行号):
        '获取指定行的长度，不包括任何尾随换行符。'
        return self.GetLineLength(行号)

    def 取指定行内容(self,行号):
        '返回文本控件中给定行的内容，不包括任何结尾的换行符。'
        return self.GetLineText(行号)

    def 取缓冲区行数(self):
        return self.GetNumberOfLines()

    def 内容是否被修改(self):
        '返回True文本是否已被用户修改。调用SetValue 不会使控件修改。'
        return self.IsModified()

    def 是否为多行编辑框(self):
        return self.IsMultiLine()

    def 是否为单行编辑框(self):
        return self.IsSingleLine()

    def 载入指定文件内容(self,路径):
        '从指定文件加载内容到编辑框'
        return self.LoadFile(路径)

    def 内容写到指定文件(self,路径):
        '将编辑框的内容写到指定文件内'
        return self.SaveFile(路径)

    def 标记为已修改2(self):
        '将文本标记为已修改'
        return self.MarkDirty()

    def 指定位置转像素位置(self,位置):
        '取指定位置处的文本的像素坐标'
        return self.PositionToCoords(位置)

    def 指定位置转行列位置(self,位置):
        '取指定位置处的文本所在行跟列,返回一个元组,(是否存在,行,列)'
        return self.PositionToXY(位置)

    def 置新文本样式(self,样式):
        '更改要用于要添加到控件的新文本的默认样式。'
        return self.SetDefaultStyle(样式)

    def 置修改状态(self,修改=True):
        '将控件标记为是否被用户修改'
        return self.SetModified(修改)

    def 标记为已修改(self):
        '将控件标记为已被用户修改'
        return self.SetModified(True)

    def 标记为未修改(self):
        '将控件标记为未被用户修改'
        return self.SetModified(False)

    def 置指定范围样式(self,开始位置,结束位置,样式):
        return self.SetStyle(开始位置,结束位置,样式)

    def 置指定位置可见(self,位置):
        '使指定位置的字符显示在编辑框可见范围内'
        return self.ShowPosition(位置)

    def 指定行列转位置(self,行,列):
        '将给定的从零开始的列和行号转换为位置'
        return self.XYToPosition(行,列)

    def 加入文本(self,内容):
        return self.write(内容)

    def 清空内容(self):
        self.Clear()

#单选框
class wx_RadioButton(wx.RadioButton,class_ec):

    def 是否选中(self):
        return self.GetValue()

    def 置选中状态(self,状态):
        'True/False'
        return self.SetValue(状态)


#多选框
class wx_CheckBox(wx.CheckBox,class_ec):

    def 取三态多选框状态(self):
        '返回 0.未选中  1.选中  2.半选中'
        return self.Get3StateValue()

    def 置三态多选框状态(self,状态):
        '0.未选中  1.选中  2.半选中'
        return self.Set3StateValue(状态)

    def 是否选中(self):
        return self.GetValue()

    def 置选中状态(self,状态):
        'True/False'
        return self.SetValue(状态)

    def 是否为三态复选框(self):
        return self.Is3State()

    def 是否可设置为半选中(self):
        return self.Is3rdStateAllowedForUser()


#图片框
class wx_StaticBitmap(wx.StaticBitmap,class_ec):

    def 取图片(self):
        '返回控件中当前使用的位图。'
        return self.GetBitmap()

    def 取图标(self):
        '返回控件中当前使用的图标。'
        return self.GetIcon()

    def 取缩放模式(self):
        '模式： 0.以原始大小显示 1.比例填充  2.通过保持纵横比，缩放位图以适合控件的大小。  3.缩放位图以填充控件的大小。'
        return self.GetScaleMode()

    def 置图片(self,图片):
        return self.SetBitmap(图片)

    def 置图标(self,图标):
        return self.SetIcon(图标)

    def 置缩放模式(self,模式):
        '模式： 0.以原始大小显示 1.比例填充  2.通过保持纵横比，缩放位图以适合控件的大小。  3.缩放位图以填充控件的大小。'
        return self.SetScaleMode(模式)

#组合框
class wx_ComboBox(wx.ComboBox,class_ec):

    def 取指定项目索引(self,项目文本,是否区分大小写=False):
        return self.FindString(项目文本,是否区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项索引(self):
        return self.GetCurrentSelection()

    def 取选中项索引2(self):
        return self.GetSelection()

    def 取选中范围(self):
        return self.GetTextSelection()

    def 取指定项目文本(self,索引):
        return self.GetString(索引)

    def 取选中项文本(self):
        return self.GetStringSelection()

    def 列表项是否为空(self):
        return self.IsListEmpty()

    def 弹出列表(self):
        self.Popup()

    def 置指定项目文本(self,索引,文本):
        self.SetString(索引,文本)

    def 置默认文本(self,文本):
        self.SetValue(文本)

    def 置选中项(self,索引):
        self.SetSelection(索引)

    def 置选中项_文本(self,项目文本):
        return self.SetStringSelection(项目文本)

    def 选中范围文本(self,开始位置,结束位置):
        '如果两个参数都等于-1，则选择控件中的所有文本'
        self.SetTextSelection(开始位置,结束位置)

    def 清空表项(self):
        self.Clear()

    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    def 删除指定项目(self,索引):
        self.Delete(索引)

    def 插入项目(self,插入位置,项目列表):
        return self.Insert(项目列表,插入位置)

#进度条
class wx_Gauge(wx.Gauge,class_ec):

    def 取最大位置(self):
        return self.GetRange()

    def 取当前位置(self):
        return self.GetValue()

    def 是否为垂直进度条(self):
        return self.IsVertical()

    def 置最大位置(self,位置):
        return self.SetRange(位置)

    def 置当前位置(self,位置):
        return self.SetValue(位置)

    def 置加载模式(self):
        '使滚动条编程滚动加载状态,调用SetValue停止滚动加载'
        self.Pulse()


#滑块条
class wx_Slider(wx.Slider,class_ec):

    def 清除刻度线(self):
        self.ClearTicks()

    def 取行大小(self):
        return self.GetLineSize()

    def 取最大位置(self):
        return self.GetMax()

    def 取最小位置(self):
        return self.GetMin()

    def 取页面间隔(self):
        return self.GetPageSize()

    def 取滑块数值范围(self):
        '返回一个元组，包含滑块的最小值跟最大值'
        return self.GetRange()

    def 取选中终点(self):
        return self.GetSelEnd()

    def 取选中起点(self):
        return self.GetSelStart()

    def 取滑块大小(self):
        return self.GetThumbLength()

    def 取刻线间隔(self):
        return self.GetTickFreq()

    def 取滑块位置(self):
        return self.GetValue()

    def 置滑块大小(self,数值):
        return self.SetThumbLength(数值)

    def 置行大小(self,数值):
        return self.SetLineSize(数值)

    def 置最大位置(self,数值):
        return self.SetMax(数值)

    def 置最小位置(self,数值):
        return self.SetMin(数值)

    def 置页面间隔(self,数值):
        return self.SetPageSize(数值)

    def 置滑块范围(self,最小值,最大值):
        return self.SetRange(最小值,最大值)

    def 置选中范围(self,起点值,结束值):
        return self.SetSelection(起点值,结束值)

    def 置刻线位置(self,位置):
        '在指定位置上标注刻线'
        return self.SetTick(位置)

    def 置刻线间隔(self,间隔):
        return self.SetTickFreq(间隔)

    def 置滑块位置(self,位置):
        return self.SetValue()


#整数微调框
class wx_SpinCtrl(wx.SpinCtrl,class_ec):

    def 取数值进制类型(self):
        '返回10或16，十进制或16进制'
        return self.GetBase()

    def 置数值进制类型(self,类型):
        '类型：10或16，十进制或16进制'
        return self.SetBase(类型)

    def 取最大值(self):
        return self.GetMax()

    def 取最小值(self):
        return self.GetMin()

    def 置最大值(self,数值):
        return self.SetMax(数值)

    def 置最小值(self,数值):
        return self.SetMin(数值)

    def 取数值范围(self):
        '获取微调的数值范围'
        return self.GetRange()

    def 置数值范围(self,最小值,最大值):
        '设置微调的数值范围'
        return self.SetRange(最小值,最大值)

    def 取当前数值():
        return self.GetValue()

    def 置当前数值(self,数值):
        return self.SetValue(数值)


#动画框
class wx_adv_AnimationCtrl(wx.adv.AnimationCtrl,class_ec):

    def 创建控件动画对象(self):
        return self.CreateCompatibleAnimation()

    def 创建控件动画对象2(self):
        return self.CreateAnimation()

    def 取当前动画(self):
        return self.GetAnimation()

    def 取当前图片(self):
        '返回当此控件显示的非活动位图；查看SetInactiveBitmap 更多信息'
        return self.GetInactiveBitmap()

    def 是否正在播放动画(self):
        return self.IsPlaying()

    def 载入动画_流(self,文件):
        '从给定的流中加载动画并调用SetAnimation'
        return self.Load(文件)

    def 载入动画_文件(self,文件):
        '从给定的文件加载动画并调用SetAnimation。'
        return self.LoadFile(文件)

    def 播放动画(self):
        return self.Play()

    def 停止播放(self):
        return self.Stop()

    def 载入动画(self,动画):
        '设置动画在此控件中播放'
        return self.SetAnimation(动画)

    def 置默认显示图片(self,图片):
        '设置位图在不播放动画时显示在控件上。'
        return self.SetInactiveBitmap(图片)


#列表框
class wx_ListBox(wx.ListBox,class_ec):

    def 取消指定选中项(self,索引):
        '在列表框中取消选择一个项目。'
        return self.Deselect(索引)

    def 保证显示(self,索引):
        '确保当前显示具有给定索引的项目。'
        return self.EnsureVisible(索引)

    def 取指定项目索引(self,查找的内容,区分大小写=False):
        '查找标签与给定字符串匹配的项目。返回项目索引'
        return self.FindString(查找的内容,区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取可见项目数(self):
        '返回可以垂直放入列表框可见区域的项目数。'
        return self.GetCountPerPage()

    def 取选中项索引(self):
        return self.GetSelection(0)

    def 取选中范围索引(self):
        '返回一个列表包含所有选中项索引,用当前所选项目的位置填充一个整数数组。'
        return self.GetSelections()

    def 取指定项目文本(self, 索引):
        return self.GetString(索引)

    def 取首个可见项索引(self):
        '返回最顶部可见项目的索引。'
        return self.GetTopItem()

    def 取指定坐标索引(self,左边,顶边):
        '返回列表框内指定坐标处项目索引'
        return self.HitTest(左边,顶边)

    def 插入项目(self,插入位置,项目列表):
        return self.InsertItems(项目列表,插入位置)

    def 清空表项(self):
        self.Clear()

    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    def 删除指定项目(self,索引):
        self.Delete(索引)

    def 项目是否选中(self,索引):
        return self.InsertItems(索引)

    def 表项是否按字母排序(self):
        return self.IsSorted()

    def 置顶指定项(self,索引):
        '将指定的项目设置为第一个可见项目。'
        self.SetFirstItem(索引)

    def 置指定项目背景色(self,索引,颜色):
        '在列表框中设置项目的背景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemBackgroundColour(索引,颜色)
        self.Refresh()

    def 置指定项目前景色(self,索引,颜色):
        '在列表框中设置项目的前景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemForegroundColour(索引,颜色)
        self.Refresh()

    def 置指定项目字体(self,索引,字体):
        '在列表框中设置项目的字体。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemFont(索引,字体)
        self.Refresh()

    def 置指定项目文本(self,索引,文本):
        self.SetString(索引,文本)

    def 置现行选中项_文本(self,项目文本):
        return self.SetStringSelection(项目文本)

    def 置现行选中项(self,索引):
        return self.SetSelection(索引)

    def 取选中项文本(self):
        return self.GetStringSelection()


#选择列表框
class wx_CheckListBox(wx.CheckListBox,class_ec):

    def 置选中状态(self,索引,选中=True):
        self.Check(索引,选中)

    def 选中项目(self,索引):
        self.Check(索引,True)

    def 取消选中项目(self,索引):
        self.Check(索引,False)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项(self):
        '返回一个元组,包含所有选中的表项索引'
        return self.GetCheckedItems()

    def 取选中项_文本(self):
        '返回一个元组,包含所有选中的表项文本'
        return self.GetCheckedStrings()

    def 是否选中(self,索引):
        return self.IsChecked(索引)

    def 置选中状态_批量(self,索引列表):
        '传入需要选中的索引列表,不存在的会报错'
        self.SetCheckedItems(索引列表)

    def 置选中状态_文本_批量(self,索引列表):
        '传入需要选中的项目文本列表,不存在的会报错'
        self.SetCheckedStrings(索引列表)

    def 置指定项目背景色(self, 索引, 颜色):
        '在列表框中设置项目的背景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemBackgroundColour(索引, 颜色)
        self.Refresh()

    def 置指定项目前景色(self, 索引, 颜色):
        '在列表框中设置项目的前景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemForegroundColour(索引, 颜色)
        self.Refresh()

    def 置指定项目字体(self, 索引, 字体):
        '在列表框中设置项目的字体。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemFont(索引, 字体)
        self.Refresh()

    def 置顶指定项(self,索引):
        '将指定的项目设置为第一个可见项目。'
        self.SetFirstItem(索引)

    def 取首个可见项索引(self):
        '返回最顶部可见项目的索引。'
        return self.GetTopItem()

    def 取指定坐标索引(self,左边,顶边):
        '返回列表框内指定坐标处项目索引'
        return self.HitTest(左边,顶边)

    def 插入项目(self,插入位置,项目列表):
        return self.Insert(项目列表,插入位置)

    def 插入项目2(self,插入位置,项目列表):
        return self.InsertItems(项目列表,插入位置)

    def 清空表项(self):
        self.Clear()

    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    def 删除指定项目(self,索引):
        self.Delete(索引)


#图形按钮
class wx_BitmapButton(wx.BitmapButton,class_ec):
    pass


#超级链接框
class wx_adv_HyperlinkCtrl(wx.adv.HyperlinkCtrl,class_ec):

    def 取单击前焦点颜色(self):
        '返回鼠标悬停在控件上时用于打印超链接标签的颜色。'
        return self.GetHoverColour()

    def 取初始颜色(self):
        '返回以前从未单击过链接（即尚未访问链接）并且鼠标不在控件上时用于打印标签的颜色。'
        return self.GetNormalColour()

    def 取URL(self):
        '返回与超链接关联的URL。'
        return self.GetURL()

    def 是否已点击(self):
        '返回True超链接是否已被用户至少单击一次。'
        return self.GetVisited()

    def 取单击后焦点颜色(self):
        '返回鼠标悬停在控件上且之前已单击链接（即已访问链接）时用于打印标签的颜色。'
        return self.GetVisitedColour()

    def 置焦点颜色(self,颜色):
        '设置鼠标悬停在控件上时用于打印超链接标签的颜色。'
        return self.SetHoverColour(颜色)

    def 置初始颜色(self,颜色):
        '设置以前从未单击过链接（即未访问链接）并且鼠标不在控件上时用于打印标签的颜色。'
        return self.SetNormalColour(颜色)

    def 置URL(self,url):
        '设置与超链接关联的URL。'
        return self.SetURL(url)

    def 置访问状态(self,已访问=True):
        '将超链接标记为已访问/未访问'
        return self.SetVisited(已访问)

    def 置已点击颜色(self,颜色):
        return self.SetVisitedColour(颜色)


#排序列表框
class wx_adv_EditableListBox(wx.adv.EditableListBox,class_ec):

    def 取项目列表(self):
        return self.GetStrings()

    def 置项目列表(self,项目列表):
        return self.SetStrings(项目列表)


#引导按钮
class wx_adv_CommandLinkButton(wx.adv.CommandLinkButton,class_ec):

    def 取主标题(self):
        return self.GetMainLabel()

    def 取描述内容(self):
        return self.GetNote()

    def 置标题(self,标题,描述):
        '要设置的标签和注释，两者之间用第一个换行符分隔，或者不设置空白注释'
        return self.SetLabel("{}\n{}".format(标题,描述))

    def 置标题2(self,标题,描述):
        return self.SetMainLabelAndNote(标题,描述)

    def 置主标题(self,标题):
        return self.SetMainLabel(标题)

    def 置描述内容(self,描述):
        return self.SetNote(描述)


#日历框
class wx_adv_CalendarCtrl(wx.adv.CalendarCtrl,class_ec):

    def 突显周末(self,突显=True):
        return self.EnableHolidayDisplay(突显)

    def 允许修改月份(self,允许=True):
        return self.EnableMonthChange(允许)

    def 取当前日期(self):
        '返回格式：2020/9/26 0:00:00'
        return self.GetDate()

    def 取可选日期范围(self):
        return self.GetDateRange()

    def 取标题背景色(self):
        return self.GetHeaderColourBg()

    def 取标题前景色(self):
        return self.GetHeaderColourFg()

    def 取背景高光颜色(self):
        return self.GetHighlightColourBg()

    def 取前景高光颜色(self):
        return self.GetHighlightColourFg()

    def 取周末突显背景色(self):
        return self.GetHolidayColourBg()

    def 取周末突显前景色(self):
        return self.GetHolidayColourFg()

    def 标记日期(self,日期,标记=True):
        '日期：0-31'
        self.Mark(日期,标记)

    def 清除指定日期属性(self,日期):
        '清除与给定日期相关联的所有属性（范围为1…31）。'
        self.ResetAttr(日期)

    def 置日期属性(self,日期,属性):
        '将属性与指定的日期关联（范围为1…31）'
        return self.SetAttr(日期,属性)

    def 置当前日期(self,日期):
        '设置当前日期。日期（wx.DateTime）'
        return self.SetDate(日期)

    def 置可选日期范围(self,最早日期,最晚日期):
        '将可以在控件中选择的日期限制为指定的范围。如果设置了任一日期，则将强制执行并True返回相应的限制。如果未设置，则现有限制将被删除并False返回。日期（wx.DateTime）'
        return self.SetDateRange(最早日期,最晚日期)

    def 置顶部颜色(self,前景色,背景色):
        '在控件顶部设置用于平日绘画的颜色。该方法当前仅在通用 wx.adv.CalendarCtrl中实现， 在本机版本中不执行任何操作。'
        return self.SetHeaderColours(前景色,背景色)

    def 置选中日期颜色(self,前景色,背景色):
        '设置用于突出显示当前所选日期的颜色。该方法当前仅在通用 wx.adv.CalendarCtrl中实现， 在本机版本中不执行任何操作。'
        return self.SetHighlightColours(前景色,背景色)

    def 某天标记为假日(self,日期):
        '将指定的日期标记为当前月份的假日。此方法仅在控件的通用版本中实现，而在本机控件中不执行任何操作。'
        return self.SetHoliday(日期)

    def 置假日突显颜色(self,前景色,背景色):
        '设置用于假日突出显示的颜色。此方法仅在控件的通用版本中实现，而在本机控件中不执行任何操作。仅当窗口样式包含 CAL_SHOW_HOLIDAYS flag或 EnableHolidayDisplay 已被调用时，才应调用它。'
        return self.SetHolidayColours(前景色,背景色)


#日期框
class wx_adv_DatePickerCtrl(wx.adv.DatePickerCtrl,class_ec):

    def 取可选日期范围(self):
        return self.GetRange()

    def 置可选日期范围(self,最早日期,最晚日期):
        return self.SetRange(最早日期,最晚日期)

    def 取当前日期(self):
        return self.GetValue()

    def 置当前日期(self,日期):
        return self.SetValue(日期)


#时间框
class wx_adv_TimePickerCtrl(wx.adv.TimePickerCtrl,class_ec):

    def 取当前时间(self):
        '返回一个元组，(时,分,秒)'
        return self.GetTime()

    def 置当前时间(self,时,分,秒):
        return self.SetTime(时,分,秒)

    def 取当前时间_dt(self):
        '返回wx.DateTime'
        return self.GetValue()

    def 置当前时间_dt(self,时间):
        'wx.DateTime格式时间'
        return self.SetValue(时间)


#滚动条
class wx_ScrollBar(wx.ScrollBar,class_ec):

    def 取页面大小(self):
        return self.GetPageSize()

    def 取最大位置(self):
        return self.GetRange()

    def 取当前位置(self):
        return self.GetThumbPosition()

    def 取滑块大小(self):
        return self.GetThumbSize()

    def 是否为垂直滚动条(self):
        return self.IsVertical()

    def 置当前位置(self,位置):
        return self.SetThumbPosition()

    def 置滚动条属性(self,当前位置,滑块大小,最大位置,页面大小,是否重绘=True):
        """
        假设您希望使用相同的字体显示50行文本。窗口的大小设置为一次只能看到16行。您将使用：
        scrollbar.SetScrollbar(0, 16, 50, 15)

        页面大小比拇指大小小1，因此上一页的最后一行将在下一页可见，以帮助定向用户
        """
        return self.SetScrollbar(当前位置,滑块大小,最大位置,页面大小,是否重绘)


#分组单选框
class wx_RadioBox(wx.RadioBox,class_ec):

    def 启用某项(self,索引):
        return self.EnableItem(索引,True)

    def 禁用某项(self,索引):
        return self.EnableItem(索引,False)

    def 置指定项是否可用(self,索引,启用=True):
        return self.EnableItem(索引, 启用)

    def 查找选项(self,标题文本,区分大小写=False):
        return self.FindString(标题文本,区分大小写)

    def 取选项列数(self):
        '返回单选框中的列数。'
        return self.GetColumnCount()

    def 取选项行数(self):
        return self.GetRowCount()

    def 取选项数(self):
        return self.GetCount()

    def 取指定坐标处选项(self,x,y):
        return self.GetItemFromPoint((x,y))

    def 取选项帮助文本(self,索引):
        return self.GetItemHelpText(索引)

    def 取选项文本(self,索引):
        return self.GetItemLabel(索引)

    def 取选项文本2(self,索引):
        return self.GetString(索引)

    def 取选项提示工具(self,索引):
        '返回与指定项目关联的工具提示（ 如果有的话）None。返回类型 wx.ToolTip'
        return self.GetItemToolTip()

    def 取选项提示文本(self,索引):
        return self.GetItemToolTip(索引).GetTip()

    def 置选项提示文本(self, 索引,提示内容):
        return self.GetItemToolTip(索引).SetTip(提示内容)

    def 置选项提示时间(self,索引,时间=2000):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetAutoPop(时间)

    def 置选项提示延迟显示时间(self, 索引, 时间):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetDelay(时间)

    def 置选项提示最大宽度(self, 索引, 宽度):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetMaxWidth(宽度)

    def 置选项提示后续提示延时(self,索引,时间):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetReshow(时间)

    def 启用或禁用选项提示(self,索引,启用=True):
        return self.GetItemToolTip(索引).Enable(启用)

    def 取现行选中项(self):
        '返回所选项目的索引，或者NOT_FOUND 如果未选择任何项目，则返回该索引 。'
        return self.GetSelection()

    def 是否启用指定项(self,索引):
        '判断指定选项是否启用,是启用不是选中'
        return self.IsItemEnabled(索引)

    def 是否显示指定项(self,索引):
        '返回True当前是否显示该项目或False是否使用隐藏该项目Show。'
        return self.IsItemShown(索引)

    def 置选项帮助文本(self,索引,内容):
        return self.SetItemHelpText(索引,内容)

    def 置选项标题(self,索引,标题):
        return self.SetItemLabel(索引,标题)

    def 置选项提示文本(self,索引,提示内容):
        return self.SetItemToolTip(索引,提示内容)

    def 置选中项(self,索引):
        '指定选项设置为选中状态'
        return self.SetSelection(索引)

    def 置选项标题(self,索引,标题):
        '指定选项设置为选中状态'
        return self.SetSelection(索引,标题)

    def 显示某项(self,索引):
        return self.ShowItem(索引,True)

    def 隐藏某项(self,索引):
        return self.ShowItem(索引,False)

    def 显示或隐藏某项(self,索引,显示=True):
        return self.ShowItem(索引,显示)


#颜色选择器
class wx_ColourPickerCtrl(wx.ColourPickerCtrl,class_ec):

    def 取当前颜色(self):
        return self.GetColour()

    def 置当前颜色(self,颜色):
        return self.SetColour(颜色)


#图文按钮
class lib_button_ThemedGenBitmapTextButton(lib_button.ThemedGenBitmapTextButton,class_ec):

    def 取禁用状态图片(self):
        return self.GetBitmapDisabled()

    def 取焦点状态图片(self):
        return self.GetBitmapFocus()

    def 取正常状态图片(self):
        return self.GetBitmapLabel()

    def 取按下状态图片(self):
        return self.GetBitmapSelected()

    def 置禁用状态图片(self):
        return self.SetBitmapDisabled()

    def 置焦点状态图片(self):
        return self.SetBitmapFocus()

    def 置正常状态图片(self):
        return self.SetBitmapLabel()

    def 置按下状态图片(self):
        return self.SetBitmapSelected()


#图文按钮L
class lib_gb_GradientButton(lib_gb.GradientButton,class_ec):

    def 是否允许通过单击获取焦点(self):
        return self.AcceptsFocus()

    def 取最佳尺寸(self):
        '返回一个元组,(宽，高),覆盖基类虚拟。根据标签和边框尺寸确定按钮的最佳尺寸。'
        return self.DoGetBestSize()

    def 取渐变底纹底端颜色(self):
        return self.GetBottomEndColour()

    def 取渐变底纹顶端颜色(self):
        return self.GetTopEndColour()

    def 取渐变底纹底部起始颜色(self):
        return self.GetBottomStartColour()

    def 取渐变底纹按下底部起始颜色(self):
        return self.GetPressedBottomColour()

    def 取渐变底纹按下顶部起始颜色(self):
        return self.GetPressedTopColour()

    def 取渐变阴影顶部起始颜色(self):
        return self.GetTopStartColour()

    def 置各状态颜色(self,起始色,前景色):
        '设置底部，顶部，按下和前景色,起始色–用于底部，顶部和压制的基础颜色,前景色 –用于文本的颜色'
        return self.SetBaseColours(起始色,前景色)

    def 置图片(self,图片):
        return self.SetBitmapLabel(图片)

    def 置渐变底纹底端颜色(self,颜色):
        return self.SetBottomEndColour(颜色)

    def 置渐变底纹顶部底部颜色(self,颜色):
        return self.SetBottomStartColour(颜色)

    def 置默认按钮(self):
        return self.SetDefault()

    def 置最佳尺寸(self):
        '将按钮调整为最佳尺寸'
        self.SetInitialSize()

    def 置渐变阴影下底部开始颜色(self,颜色):
        return self.SetPressedBottomColour(颜色)

    def 置渐变阴影设置按下顶部起始颜色(self,颜色):
        return self.SetPressedTopColour(颜色)

    def 置渐变底纹顶端颜色(self,颜色):
        return self.SetTopEndColour(颜色)

    def 置渐变底纹顶部起始颜色(self,颜色):
        return self.SetTopStartColour(颜色)


#超级链接框L
class lib_hyperlink_HyperLinkCtrl(lib_hyperlink.HyperLinkCtrl,class_ec):

    def 允许打开链接(self,打开=True):
        '单击后自动浏览到URL。'
        return self.AutoBrowse(True)

    def 弹出错误提示(self,提示内容):
        return self.DisplayError(提示内容)

    def 允许右键弹出菜单(self,弹出=True):
        return self.DoPopup(弹出)

    def 允许翻转(self,允许=False):
        '干啥用的'
        return self.EnableRollover(允许)

    def 标题是否为粗体(self):
        return self.GetBold()

    def 取默认字体颜色(self):
        return self.GetColours()[0]

    def 取访问后字体颜色(self):
        return self.GetColours()[1]

    def 取焦点字体颜色(self):
        return self.GetColours()[2]

    def 取各种字体颜色(self):
        '返回一个元组,(默认颜色,点击后颜色,焦点颜色)'
        return self.GetColours()

    def 默认标题是否带下划线(self):
        return self.GetUnderlines()[0]

    def 焦点标题是否带下划线(self):
        return self.GetUnderlines()[1]

    def 点击后标题是否带下划线(self):
        return self.GetUnderlines()[2]

    def 标题是否带各状态下划线(self):
        '返回一个元组，显示各状态下标题是否带下划线,（默认标题，焦点状态标题，点击后标题）'
        return self.GetUnderlines()

    def 取鼠标光标(self):
        return self.GetLinkCursor()

    def 取URL(self):
        return self.GetURL()

    def 是否已访问过(self):
        return self.GetVisited()

    def 打开指定链接(self,链接):
        return self.GotoURL(链接)

    def 置标题字体粗细(self,粗体=True):
        return self.SetBold(粗体)

    def 置各状态标题颜色(self,默认,访问后,焦点):
        '设置链接，访问的链接和鼠标悬停的颜色。'
        return self.SetColours(默认,访问后,焦点)

    def 置默认标题颜色(self,颜色):
        return self.SetColours(颜色,None,None)

    def 置访问后标题颜色(self,颜色):
        return self.SetColours(None,颜色,None)

    def 置焦点标题颜色(self, 颜色):
        return self.SetColours(None, None, 颜色)

    def 置各状态标题下划线(self,默认=False,已访问=False,焦点=False):
        '设置是否应为新链接，访问的链接和过渡文本加下划线。'
        return self.SetUnderlines(默认,已访问,焦点)

    def 置默认标题下划线(self,下划线=True):
        return self.SetUnderlines(下划线,None,None)

    def 置访问猴标题下划线(self,下划线=True):
        return self.SetUnderlines(None,下划线,None)

    def 置焦点标题下划线(self,下划线=True):
        return self.SetUnderlines(None,None,下划线)

    def 置URL(self,url):
        return self.SetURL(url)

    def 置访问状态(self,状态=True):
        '设置链接访问状态是否已访问郭'
        return self.SetVisited(状态)

    def 更新链接(self,刷新控件=True):
        self.UpdateLink(刷新控件)


#小数微调框
class lib_fs_FloatSpin(lib_fs.FloatSpin,class_ec):

    def 取当前数值(self):
        return self.GetDefaultValue().GetValue()

    def 取当前数值2(self):
        return self.GetValue()

    def 取默认数值(self):
        return self.GetDefaultValue()

    def 取显示的位数(self):
        return self.GetDigits()

    def 取字符格式(self):
        return self.GetFormat()

    def 取最大值(self):
        return self.GetMax()

    def 取最小值(self):
        return self.GetMin()

    def 置最大值(self,最大值):
        return self.SetMax(最大值)

    def 置最小值(self,最小值):
        return self.SetMin(最小值)

    def 置数值范围(self,最小值,最大值):
        return self.SetRange(最小值,最大值)

    def 置数值范围2(self,最小值,最大值):
        return self.SetRangeDontClampValue(最小值,最大值)

    def 是否设置数值范围(self):
        return self.HasRange()

    def 是否在数值范围内容(self,数值):
        '测试指定数值是否在允许的范围内'
        return self.InRange(数值)

    def 是否已设置默认值(self):
        return self.IsDefaultValue()

    def 置小数位数(self,位数):
        return self.SetDigits(位数)

    def 置字符格式(self,格式):
        return self.SetFormat(格式)

    def 置当前数值(self,数值):
        return self.SetValue(数值)

#超级列表框
class wx_ListCtrl(wx.ListCtrl,class_ec):

    def 加入行(self,内容列表):
        '在末尾加入新一行数据，返回加入的行索引'
        return self.Append(内容列表)

    def 加入列(self,标题,对齐方式=2,宽度=-1):
        """
        在末尾加入新一列
        :param 标题: 自己定
        :param 对齐方式: 0.左对齐  1.右对齐 2.居中
        :param 宽度: 自己定
        :return:加入的列索引
        """
        return self.AppendColumn(标题,对齐方式,宽度)

    def 排列项目(self,排列方式=0):
        """
        在图标或小图标视图中排列项目
        :param 排列方式: 0.默认对齐方式  1.与控件的左侧对齐 2.与控件的顶部对齐 3.对齐网格
        :return:
        """
        return self.Arrange(排列方式)

    def 置选中状态(self,索引,选中=True):
        '使用复选框选中或取消选中 控件中的wx.ListItem'
        return self.CheckItem(索引,选中)

    def 全部删除(self):
        '删除所有项目和所有列'
        return self.ClearAll()

    def 删除所有列(self):
        return self.DeleteAllColumns()

    def 删除所有行(self):
        return self.DeleteAllItems()

    def 删除指定列(self,列索引):
        return self.DeleteColumn(列索引)

    def 删除指定行(self,行索引):
        return self.DeleteItem(行索引)

    def 开始编辑(self,行索引):
        '需要设置了 wx.LC_EDIT_LABELS 样式才能使用,开始编辑指定行的第一列'
        return self.EditLabel(行索引)

    def 启用或禁用交替行背景色(self,启用=True):
        '启用交替的行背景色（也称为斑马条纹）,该方法只能在虚拟报表模式（即具有LC_REPORT 和LC_VIRTUAL 样式）中为控件调用。'
        return self.EnableAlternateRowColours(启用)

    def 启用或禁用按键搜索(self,启用):
        '只匹配第一列，从键盘搜索项目时，如果当前输入的文本不匹配，则启用或禁用蜂鸣声。'
        return self.EnableBellOnNoMatch(启用)

    def 启用或禁用选择框(self,启用=True):
        '启用或禁用列表项的复选框'
        return self.EnableCheckBoxes(启用)

    def 启用或禁用系统主题样式(self,启用=True):
        return self.EnableSystemTheme(启用)

    def 保证显示(self,行索引):
        return self.EnsureVisible(行索引)

    def 保证显示2(self,行索引):
        return self.Focus(行索引)

    def 查找表项(self,查找的内容,开始索引=-1,模糊查找=False):
        '只查找第一列'
        return self.FindItem(开始索引,查找的内容,模糊查找)

    def 取交替行背景色(self):
        return self.GetAlternateRowColour()

    def 取列对象(self,列索引):
        return self.GetColumn(列索引)

    def 取列标题(self,列索引):
        return self.GetColumn(列索引).GetText()

    def 取列对齐方式(self,列索引):
        "对齐方式：0.左对齐 1.右对齐 2.居中"
        return self.GetColumn(列索引).GetAlign()

    def 取列宽(self,列索引):
        return self.GetColumnWidth(列索引)

    def 取列宽2(self,列索引):
        return self.GetColumn(列索引).GetWidth()

    def 取列数(self):
        return self.GetColumnCount()

    def 取可视列索引(self,索引):
        '一般用不上，除非你调整了列排序啥的我也没用过'
        return self.GetColumnOrder(索引)

    def 取列顺序索引(self):
        '一般用不上除非你改动了列，返回一个列表，包含列索引数值'
        return self.GetColumnsOrder()

    def 取可见行数(self):
        '返回列表框完全可见的行数'
        return self.GetCountPerPage()

    def 取编辑控件对象(self):
        '返回当前用于编辑标签的编辑控件。None如果没有标签被编辑，则返回'
        return self.GetEditControl()

    def 取现行选中项(self):
        '返回第一个选定的项目；如果未选择任何项目，则返回-1。'
        return self.GetFirstSelected()

    def 取现行焦点项(self):
        '获取当前焦点的项目；如果没有焦点，则返回-1。'
        return self.GetFocusedItem()

    def 取图片组列表(self,类型):
        '图片组类型：0.普通(大图列表)  1.小图列表  2.自定义列表  返回类型wx.ImageList'
        return self.GetImageList(类型)

    def 取行数(self):
        return self.GetItemCount()

    def 取行对象(self,行索引):
        return self.GetItem(行索引)

    def 取行背景色(self,行索引):
        return self.GetItemBackgroundColour(行索引)

    def 取行背景色2(self,行索引):
        return self.GetItem(行索引).GetBackgroundColour()

    def 取行字体(self,行索引):
        return self.GetItemFont(行索引)

    def 取行坐标(self,行索引):
        '返回指定行所在的x,y坐标'
        return self.GetItemPosition(行索引)

    def 取行矩形(self,行索引):
        '返回指定行的矩形'
        return self.GetItemRect(行索引)

    def 取图标间距(self):
        return self.GetItemSpacing()

    def 取行状态(self,行索引,类型=wx.LIST_STATE_SELECTED):
        '默认返回是否为现行选中项'
        return bool(self.GetItemState(行索引,类型))

    def 取标题(self,行索引,列索引):
        return self.GetItemText(行索引,列索引)

    def 取行文本颜色(self,行索引):
        '如果项目没有特定的颜色，则返回无效的颜色（而不是控件本身的默认前景色控件，因为这不允许区分与当前控件前景色相同颜色的项目和默认颜色的项目，因此，与控件始终具有相同的颜色）。'
        return self.GetItemTextColour(行索引)

    def 取下一选中项(self,当前索引):
        '返回指定行下面的现行选中项 没有就返回-1'
        return self.GetNextSelected(当前索引)

    def 取选中表项数(self):
        return self.GetSelectedItemCount()

    def 取文本颜色(self):
        return self.GetTextColour()

    def 取首个可见索引(self):
        '在列表或报表视图中获取最顶部可见项目的索引。'
        return self.GetTopItem()

    def 取最大尺寸(self):
        '''
        请注意，此功能仅在图标视图和小图标视图中有效，而在列表视图或报表视图中则无效（这是本机Win32控件的限制）。
        返回控件中所有项目采用的矩形。
        换句话说，如果控件客户端的大小等于此矩形的大小，则不需要滚动条，也不会留下可用空间。
        '''
        return self.GetViewRect()

    def 是否启用选择框(self):
        return self.HasCheckBoxes()

    def 是否带LC_REPORT样式(self):
        '单列或多列报表视图，带有可选标题。'
        return self.InReportView()

    def 插入列(self,插入位置,标题,对齐方式=2,宽度=-1):
        """
        在末尾加入新一列
        :param 标题: 自己定
        :param 对齐方式: 0.左对齐  1.右对齐 2.居中
        :param 宽度: 自己定
        :return:加入的列索引
        """
        return self.InsertColumn(插入位置,标题,对齐方式,宽度)

    def 插入行(self,插入位置,标题):
        '只能插入第一个标题'
        return self.InsertItem(插入位置,标题)

    def 插入图片(self,插入位置,图片索引):
        '与此控件和视图样式关联的图像列表的索引'
        return self.InsertItem(插入位置,图片索引)

    def 插入图文(self,插入位置,标题,图片索引):
        '插入图像/字符串项目。'
        return self.InsertItem(插入位置, 标题,图片索引)

    def 是否无表项(self):
        '具有某些列的控件如果没有行，则仍被认为是空的。'
        return self.IsEmpty()

    def 是否选中(self,行索引):
        '判断该行选择框是否勾选'
        return self.IsItemChecked(行索引)

    def 是否为选择项(self,索引):
        '返回True是否选择了该项目,不是选中'
        return self.IsSelected(索引)

    def 是否为虚拟报表(self):
        '返回True该控件当前是否在虚拟报表视图中。'
        return self.IsVirtual()

    def 表项是否可见(self,行索引):
        '检查项目是否可见。'
        return self.IsVisible(行索引)

    def 取指定行图片索引(self,行索引):
        '它应返回控件图像列表中项目图像的索引，如果没有图像，则返回-1'
        return self.OnGetItemImage(行索引)

    def 是否选中2(self,行索引):
        '它应该返回是否选中了指定 item 复选框。对于具有 使用复选框的样式的控件，必须在派生类中重写 此函数LC_VIRTUAL。'
        return self.OnGetItemIsChecked(行索引)

    def 取标题2(self,行索引,列索引):
        '它应返回包含 指定 的给定列文本的字符串item。对于具有 样式的控件，必须在派生类中重写 此函数LC_VIRTUAL。'
        return self.OnGetItemText(行索引,列索引)

    def 重画指定项目(self,行索引):
        return self.RefreshItem(行索引)

    def 重画指定范围项目(self,起始行,结束行):
        '正如RefreshItem 这仅对虚拟列表控件有用。起始项必须小于或等于结束项。重绘itemFrom 和itemTo之间的项目。'
        return self.RefreshItems(起始行,结束行)

    def 滚动滚动条(self,dx,dy):
        '如果处于图标，小图标或报告查看模式，则dx 指定要滚动的像素数。如果处于列表视图模式，则dx 指定要滚动的列数。dy 始终指定要垂直滚动的像素数。'
        return self.ScrollList(dx,dy)

    def 选择某项(self,行索引):
        '选择不是选中'
        return self.Select(行索引)

    def 置备用行背景色(self,颜色):
        '将备用行背景色设置为特定颜色。与一样EnableAlternateRowColours，此方法只能与具有LC_REPORT 和LC_VIRTUAL 样式的控件一起使用'
        return self.SetAlternateRowColour(颜色)

    def 置列标题(self,列索引,标题):
        Item = self.GetColumn(列索引)
        Item.SetText(标题)
        return self.SetColumn(列索引,Item)

    def 置列宽(self,列索引,宽度):
        return self.SetColumnWidth(列索引,宽度)

    def 置列宽2(self,列索引,宽度):
        Item = self.GetColumn(列索引)
        Item.SetWidth(宽度)
        return self.SetColumn(列索引,Item)

    def 置列对齐方式(self,列索引,对齐方式):
        '对齐方式: 0.左对齐  1.右对齐 2.居中'
        Item = self.GetColumn(列索引)
        Item.SetAlign(对齐方式)
        return self.SetColumn(列索引,Item)

    def 置列图片(self,列索引,图片):
        return self.SetColumnImage(列索引,图片)

    def 置列排序位置(self,排序列表):
        '修改列的位置'
        return self.SetColumnsOrder(排序列表)

    def 置列标题字体颜色(self,attr):
        '更改用于列表控件标题的字体和颜色。'
        return self.SetHeaderAttr(attr)

    def 置关联图片列表(self,图片列表):
        return self.SetImageList(图片列表)

    def 置标题(self,行索引,列索引,标题):
        return self.SetItem(行索引,列索引,标题)

    def 置图文(self,行索引,列索引,标题,图片索引):
        return self.SetItem(行索引,列索引,标题,图片索引)

    def 置行色(self,行索引,颜色):
        return self.SetItemBackgroundColour(行索引,颜色)

    def 置图片(self,行索引,列索引,图片索引):
        return self.SetItemColumnImage(行索引,列索引,图片索引)

    def 置行数(self,行数):
        '此方法只能与虚拟列表控件一起使用。 没用过'
        return self.SetItemCount(行数)

    def 置行字体(self,行索引,字体):
        return self.SetItemFont(行索引,字体)

    def 置选中状态图片(self,行索引,选中图索引,未选中图索引):
        '设置与项目关联的未选择和选择的图像。'
        return self.SetItemImage(行索引,选中图索引,未选中图索引)

    def 置项目坐标(self,项目索引,x,y):
        '在图标或小图标视图中设置项目的位置。'
        return self.SetItemPosition(项目索引,(x,y))

    def 置选择状态(self,行索引,是否选择):
        状态 = 4 if 是否选择 else 0
        return self.SetItemState(行索引, 状态, wx.LIST_STATE_SELECTED)

    def 置标题_首列(self,行索引,标题):
        return self.SetItemText(行索引,标题)

    def 置行文本颜色(self,行索引,颜色):
        return self.SetItemTextColour(行索引,颜色)

    def 添加列表样式(self,样式):
        return self.SetSingleStyle(样式,True)

    def 删除列表样式(self,样式):
        return self.SetSingleStyle(样式,False)

    def 置全部文本颜色(self,颜色):
        return self.SetTextColour(颜色)

    def 置窗口新样式(self,样式):
        return self.SetWindowStyleFlag(样式)

if __name__ == '__main__':
    print("在线文档：http://012.plus/pyec/")