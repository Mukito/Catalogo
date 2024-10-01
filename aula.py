import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.AUTO

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5
        main_image.update()
        options.update()



    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='poltrona_amarela.jpeg'
                ),
                
                
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='poltrona_amarela.jpeg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                             
                        ),
                        ft.Container(
                            image_src='poltrona_azul_marinho.jpeg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image    
                        ),
                        ft.Container(
                            image_src='poltrona_preta.jpeg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image    
                        )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='CADEIRAS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    value='Poltrona Amarela Moderna',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30
                ),
                ft.Text(
                    value='Sala de Estar',
                    color=ft.colors.GREY,
                    italic=True,
                ),
                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs':12, 'sm': 6},
                            value='R$ 399',
                            color=ft.colors.WHITE,
                            size=30
                        ),
                        ft.Row(
                            col={'xs':12, 'sm': 6},
                            spacing=5,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range (5)
                            ]
                        )
                    ]
                ),

                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Poltrona Decorativa Opalla Salão Suede Amarela - Kimi Design Nossa empresa já estão a alguns anos no segmento, apenas com a loja física, e agora também atendendo nos principais marketplace’s do Brasil. ',
                                    color= ft.colors.GREY,
                                )
                            )    
                        ),

                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Altura total: 93cm;Largura total: 85cm;Profundidade total: 73cm;Largura do assento: 50x45; Largura do encosto: 50x45;Altura dos pés: 30cm;Peso: 16kg. Limpeza: Utilizar um pano limpo e seco. Não limpar com produtos abrasivos ou escovas',
                                    color= ft.colors.GREY,
                                )
                            )
                        )
                    ]
                ),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Cor',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Amarelo'),
                                ft.dropdown.Option(text='Azul'),
                                ft.dropdown.Option(text='Preta'),
                            ]
                        ),

                        ft.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[

                                ft.dropdown.Option(text=f'{num} unid.') for num in range(1, 11)
                                
                            ]
                        ),
                    ]

                ),
                ft.Container(expand=True),

                ft.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.WHITE
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK
                        }

                    )
                ),
                
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao Carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER)
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.AMBER
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK
                        }

                    )
                )
            ]
        )
    )
   
    layout = ft.Container(
        width=900,
        #height=200,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)