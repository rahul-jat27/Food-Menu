from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.fitimage import FitImage
from kivy.lang.builder import Builder
from kivymd.uix.widget import MDWidget
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield.textfield import MDTextField
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList,OneLineIconListItem
from kivymd.uix.list import IconLeftWidgetWithoutTouch
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.stacklayout import StackLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout


# Set the Window Size
Window.size=(1280,800)
class Items_of_Menu(MDBoxLayout):
    list_information = {"checkboxes": [], "labels": [], "quantity": []}
    selected_items = {"checkboxes": [], "labels": [], "quantity": []}
    def __init__(self,**kwargs):
        super(Items_of_Menu,self).__init__(**kwargs)
        scrollbarwin=ScrollView()

        content_box=BoxLayout(orientation='vertical',padding=dp(8),spacing=dp(8),size_hint=(1,None))
        content_box.bind(minimum_height=content_box.setter('height'))

        # for loop which is used for adding the items in the as a list
        for i in range(10):
            Template_card= Elevation(
                size_hint_y=None,
                size_hint_x=.960,
                height = dp(100),
                padding = dp(4),
                pos_hint={'center_y': .5, 'center_x': .490},
                radius = [20,],
                elevation = 4,

            )
            checkbox=MDCheckbox(
                size_hint=(None, None),
                size= (dp(48),dp(48)),
                pos_hint={'center_y': .5}
            )
            checkbox.bind(active=lambda instance,value:self.Selected_checkbox(instance,value))
            self.list_information["checkboxes"].append(checkbox)
            image_box=MDBoxLayout(adaptive_size=True)
            image=FitImage(
                source="D:/Study/Python/Kivy/images/2.jpg",
                size_hint= (None, None),
                height=dp(80),
                width=dp(130),
                radius=[12,],
                pos_hint={'center_y':0.5}

            )
            image_box.add_widget(image)
            text_box=MDBoxLayout(orientation="vertical",adaptive_height=True,pos_hint={'center_y':0.5},padding=[12,0,0,0])
            item_name=MDLabel(text=f"item{i}",font_style="H5",size_hint=(1,None),bold=True,theme_text_color="Primary")
            item_name.bind(texture_size=item_name.setter('size'))
            self.list_information["labels"].append(item_name)
            price=MDLabel(text=u"Price: \u20B9400/per",font_style="Subtitle1",size_hint=(1,None),bold=True,theme_text_color="Hint")
            price.bind(texture_size=price.setter('size'))
            quantitybox=MDBoxLayout(orientation='vertical',adaptive_height=True,size_hint_x=0.2,pos_hint = {'center_y': .5,'center_x':0.5})
            quantityfield=MDTextField(
                hint_text= "Quantity",
                mode= "rectangle",
                size_hint=(None,None),
                width=dp(80),
                height= dp(40),
                padding=[0,0,15,0]
            )
            self.list_information["quantity"].append(quantityfield)
            quantitybox.add_widget(quantityfield)
            Template_card.add_widget(checkbox)
            Template_card.add_widget(image_box)
            Template_card.add_widget(text_box)
            text_box.add_widget(item_name)
            text_box.add_widget(price)
            Template_card.add_widget(quantitybox)
            content_box.add_widget(Template_card)
        scrollbarwin.add_widget(content_box)
        self.add_widget(scrollbarwin)
    def Selected_checkbox(self,instance,value):
        for i in range(0,len(Items_of_Menu.list_information["checkboxes"])):
            if instance==Items_of_Menu.list_information["checkboxes"][i] and value== True:
                self.selected_items["labels"].append(self.list_information["labels"][i])
                self.selected_items["quantity"].append(self.list_information["quantity"][i])
            elif instance==Items_of_Menu.list_information["checkboxes"][i] and value== False :
                self.selected_items["labels"].remove(self.list_information["labels"][i])
                self.selected_items["quantity"].remove(self.list_information["quantity"][i])
        





class navigation(Screen):
    def __init__(self,**kwargs):
        super(navigation,self).__init__(**kwargs)

        # Navigation Layout
        nav_layout=MDNavigationLayout()

        # Theme Color
        theme=ThemableBehavior()

        # Screen Manager
        scr_mang=ScreenManager()

        # Navigation Drawer
        nav_drawer=MDNavigationDrawer()

        # List of Items
        self.list_for_item=MDList()

        # Put Items in List
        #1
        icon_image = IconLeftWidgetWithoutTouch(icon="food")
        item_list = OneLineIconListItem(text="Main Course", theme_text_color="Custom", text_color=theme.theme_cls.text_color)
        item_list.add_widget(icon_image)
        item_list.bind(on_release=lambda x: self.Change_Screen(x))
        self.list_for_item.add_widget(item_list)
        #2
        icon_image2 = IconLeftWidgetWithoutTouch(icon="coffee")
        item2_list = OneLineIconListItem(text="Tea and Coffee", theme_text_color="Custom", text_color=theme.theme_cls.text_color)
        item2_list.add_widget(icon_image2)
        item2_list.bind(on_release=lambda x: self.Change_Screen(x))
        self.list_for_item.add_widget(item2_list)
        #3
        icon_image3 = IconLeftWidgetWithoutTouch(icon="ice-cream")
        item3_list = OneLineIconListItem(text="Ice Creams", theme_text_color="Custom", text_color=theme.theme_cls.text_color)
        item3_list.add_widget(icon_image3)
        item3_list.bind(on_release=lambda x: self.Change_Screen(x))
        self.list_for_item.add_widget(item3_list)
        #4
        icon_image4 = IconLeftWidgetWithoutTouch(icon="bottle-soda")
        item4_list = OneLineIconListItem(text="Cold Drinks", theme_text_color="Custom", text_color=theme.theme_cls.text_color)
        item4_list.add_widget(icon_image4)
        item4_list.bind(on_release=lambda x: self.Change_Screen(x))
        self.list_for_item.add_widget(item4_list)
        #5
        icon_image5 = IconLeftWidgetWithoutTouch(icon="hamburger")
        item5_list = OneLineIconListItem(text="Fast Food", theme_text_color="Custom", text_color=theme.theme_cls.text_color)
        item5_list.add_widget(icon_image5)
        item5_list.bind(on_release=lambda x: self.Change_Screen(x))
        self.list_for_item.add_widget(item5_list)
        #6
        icon_image6 = IconLeftWidgetWithoutTouch(icon="food-takeout-box")
        item6_list = OneLineIconListItem(text="Special Dishes", theme_text_color="Custom", text_color=theme.theme_cls.text_color)
        item6_list.add_widget(icon_image6)
        item6_list.bind(on_release=lambda x: self.Change_Screen(x))
        self.list_for_item.add_widget(item6_list)

        # Whole Content box is here
        content_box=MDBoxLayout(orientation="vertical",spacing=dp(8),padding=dp(8))

        # Screen Stuff is here
        items_part=Items_of_Menu()




        # Hotel Information
        hotel_image=FitImage(source="Hotel logo.jpg",radius=[100,100,100,100],size_hint=(None,None),size=(dp(100),dp(100)),pos_hint={"center_x":0.5})
        hotel_name=MDLabel(text="Hotel Heera Panna and Family Restaurant",size_hint=(1,None))
        hotel_name.font_style="Subtitle2"
        hotel_name.bind(texture_size=hotel_name.setter("size"))

        # Email Info
        email = MDLabel(text="rahuljatajoliyajat@gmail.com", size_hint=(1,None))
        email.bind(texture_size=email.setter("size"))
        email.font_style="Caption"

        # ScrollBar for Items of List in Navigation Drawer
        nav_scroll=ScrollView()

        # Screen which is a child of  Whole Content Box
        scr=Screen()

        # the Top Toolbar  of the Window(Header)
        box=MDBoxLayout(orientation="vertical")
        self.toolbar=MDTopAppBar(title="Demo App",left_action_items=[["menu",lambda x:nav_drawer.set_state("open")]],
                                 right_action_items=[ ["information-outline",lambda x:self.right_hand_side_buttons("Description of food"),"Description of food"],
                                ["food-off-outline", "Order Cancel"],
                                ["book-edit", lambda x:x, "Current Bill"],
                                ["credit-card-outline", lambda x:x, "Make Payment"],],elevation=10,use_overflow=True)


        # Adding the Child Widget to the Parent Widget
        box.add_widget(self.toolbar)
        box.add_widget(items_part)
        scr.add_widget(box)
        scr_mang.add_widget(scr)
        nav_layout.add_widget(scr_mang)
        content_box.add_widget(hotel_image)
        content_box.add_widget(hotel_name)
        content_box.add_widget(email)
        nav_scroll.add_widget(self.list_for_item)
        content_box.add_widget(nav_scroll)
        nav_drawer.add_widget(content_box)
        nav_layout.add_widget(nav_drawer)
        self.add_widget(nav_layout)
    def Change_Screen(self,instance):
        value=instance.text
        if MymdCard.sm.current_screen!=value:
            MymdCard.sm.current=value
    def right_hand_side_buttons(self,button):
        MymdCard.sm.current=button
class Description_item(Screen):
    def __init__(self,**kwargs):
        super(Description_item,self).__init__(**kwargs)

        print(Items_of_Menu.selected_items)
        wholeContentBoxContainer=MDBoxLayout(orientation="vertical")

        for item in range(0,len(Items_of_Menu.selected_items["labels"])):
                label=MDLabel(text=Items_of_Menu.selected_items["labels"][item].text)
                print(Items_of_Menu.selected_items["labels"][item].text)
                quantity=MDLabel(text=Items_of_Menu.selected_items["quantity"][item].text)
                wholeContentBoxContainer.add_widget(label)
                wholeContentBoxContainer.add_widget(quantity)
        self.add_widget(wholeContentBoxContainer)
    pass






class mainHeading(MDWidget,Widget):
    pass

class Elevation(RoundedRectangularElevationBehavior,MDCard):
    pass


class FirstWin(RoundedRectangularElevationBehavior,Screen,mainHeading):
    textAndImageReference={"main_txt":[],"image":[],"hint_txt":[]}

    Category_names=["Main Course","Tea and Coffee","Ice Creams","Cold Drinks","Fast Food","Special Dishes"]
    def __init__(self,**kwargs):
        super(FirstWin,self).__init__(**kwargs)
        scrollbar=ScrollView(size_hint_y=None,pos_hint={'x':0,'top':0.850},size=(Window.width,Window.height))
        secondary_widget=StackLayout(size_hint=(1,None),spacing=50,padding=20)
        secondary_widget.bind(minimum_height=secondary_widget.setter('height'))
        for i in range(0,len(self.Category_names)):
            mycard=Elevation(
                elevation=15,
                size_hint =(0.2,None),
                height=350,
                orientation='vertical',
                radius= [36, ],
                ripple_behavior=True,
                focus_behavior=True

            )
            mycard.bind(size=self.adjust_sizes)
            image = FitImage(radius=[36,36,0,0],size_hint_y=3, size_hint_x=1,orientation="vertical")
            imagebutton = Button(background_normal="D:/Study/Python/Kivy/images/1.jpg",
                                 background_down="D:/Study/Python/Kivy/images/1.jpg",
                                 size_hint_y=550.0,
                                 size_hint_x=1,
                                 pos_hint={'x': 0, 'y': 0}
                                 )
            self.textAndImageReference["image"].append(imagebutton)
            imagebutton.bind(on_release=lambda x:self.Change_Menu_category(x))
            texture_part = MDBoxLayout( md_bg_color=(46 / 255, 8 / 255, 211 / 255, .5),
                                         radius=[0, 0, 36, 36],orientation="vertical")
            main_text = Button(
                text=self.Category_names[i],
                halign="center",
                bold=True,
                font_size=mycard.width /6,
                background_normal='',
                background_color=(0, 0, 0, 0)
            )
            self.textAndImageReference["main_txt"].append(main_text)
            main_text.bind(on_release=lambda x:self.Change_Menu_category(x))
            Hint_text = Button(
                text="Food Menu",
                halign="center",
                font_size=mycard.width/6,
                bold=True,
                color=(206 / 255, 203 / 255, 203 / 255, 0.2),
                background_normal='',
                background_color=(0, 0, 0, 0)
            )
            self.textAndImageReference["hint_txt"].append(Hint_text)
            Hint_text.bind(on_release=lambda x:self.Change_Menu_category(x))
            image.add_widget(imagebutton)
            mycard.add_widget(image)
            texture_part.add_widget(main_text)
            texture_part.add_widget(Hint_text)
            mycard.add_widget(texture_part)
            secondary_widget.add_widget(mycard)
        last_one=MDBoxLayout(size_hint=(1,None),height=20)
        secondary_widget.add_widget(last_one)
        scrollbar.add_widget(secondary_widget)

        self.add_widget(scrollbar)

    def adjust_sizes(self, mycard, new_size):
        for i in range(0,len(self.textAndImageReference["main_txt"])):
            self.textAndImageReference["main_txt"][i].font_size =mycard.width/10
            self.textAndImageReference["hint_txt"][i].font_size =mycard.width/15
    def Change_Menu_category(self,instance):
        for i in range(0,len(self.textAndImageReference["main_txt"])):
            if instance==self.textAndImageReference["main_txt"][i]:
                item=self.textAndImageReference["main_txt"][i].text
                MymdCard.sm.current=item
            elif instance==self.textAndImageReference["hint_txt"][i]:
                item=self.textAndImageReference["main_txt"][i].text
                MymdCard.sm.current=item
            elif instance==self.textAndImageReference["image"][i]:
                item=self.textAndImageReference["main_txt"][i].text
                MymdCard.sm.current=item



class Main_Course(navigation):
    def __init__(self,**kwargs):
        super(Main_Course,self).__init__(**kwargs)
        name="Main Course"
        color=ThemableBehavior()
        self.toolbar.title=name
        for item in self.list_for_item.children:
            if item.text==name:
                item.text_color=color.theme_cls.primary_color

class Tea_Coffee(navigation):
    def __init__(self, **kwargs):
        super(Tea_Coffee, self).__init__(**kwargs)

        name = "Tea and Coffee"
        color = ThemableBehavior()
        self.toolbar.title = name
        for item in self.list_for_item.children:
            if item.text == name:
                item.text_color = color.theme_cls.primary_color
class Ice_creams(navigation):
    def __init__(self, **kwargs):
        super(Ice_creams, self).__init__(**kwargs)

        name = "Ice Creams"
        color = ThemableBehavior()
        self.toolbar.title = name
        for item in self.list_for_item.children:
            if item.text == name:
                item.text_color = color.theme_cls.primary_color
class Cold_drinks(navigation):
    def __init__(self, **kwargs):
        super(Cold_drinks, self).__init__(**kwargs)

        name = "Cold Drinks"
        color = ThemableBehavior()
        self.toolbar.title = name
        for item in self.list_for_item.children:
            if item.text == name:
                item.text_color = color.theme_cls.primary_color
class Fast_food(navigation):
    def __init__(self, **kwargs):
        super(Fast_food, self).__init__(**kwargs)

        name = "Fast Food"
        color = ThemableBehavior()
        self.toolbar.title = name
        for item in self.list_for_item.children:
            if item.text == name:
                item.text_color = color.theme_cls.primary_color
class Special_dishes(navigation):
    def __init__(self, **kwargs):
        super(Special_dishes, self).__init__(**kwargs)

        name = "Special Dishes"
        color = ThemableBehavior()
        self.toolbar.title = name
        for item in self.list_for_item.children:
            if item.text == name:
                item.text_color = color.theme_cls.primary_color
class MymdCard(MDApp):
    sm=ScreenManager()
    def build(self):

        Builder.load_file("md_card_py.kv")
        self.theme_cls.theme_style = "Dark"
        Screens=[FirstWin(name='Menu_category'),Main_Course(name="Main Course"),Tea_Coffee(name="Tea and Coffee"),Ice_creams(name="Ice Creams"),Cold_drinks(name="Cold Drinks"),Fast_food(name="Fast Food"),Special_dishes(name="Special Dishes"),Description_item(name="Description of food")]
        for screen in Screens:
            self.sm.add_widget(screen)
        return self.sm




if __name__ == '__main__':

    MymdCard().run()

