export interface Articulo {
  id?: number
  descripcion: string
  precio: number
  stock: number
  marca_id: number
  proveedor_id: number
  categorias: number[] 
}

export interface ArticuloConInfo extends Articulo {
  marca: string
  proveedor: string
  categorias_nombres: string[]
}