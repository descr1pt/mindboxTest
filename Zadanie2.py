from pyspark.shell import spark


def get_product_category_pairs(products_df, categories_df):
    # Сделаем объединение продуктов с категориями по общему столбцу
    joined_df = products_df.join(categories_df, 'product_id', 'left_outer')

    # Выберем пары "Имя продукта - Имя категории"
    product_category_pairs = joined_df.select('product_name', 'category_name')

    # Выберем продукты, у которых нет категорий
    products_with_no_category = products_df.join(categories_df, 'product_id', 'left_anti').select('product_name')

    return product_category_pairs, products_with_no_category


# Пример использования метода
products_df = spark.createDataFrame([
    (1, "Product A"),
    (2, "Product B"),
    (3, "Product C")
], ["product_id", "product_name"])

categories_df = spark.createDataFrame([
    (1, "Category X"),
    (2, "Category Y"),
    (3, "Category Z"),
    (4, "Category W")
], ["product_id", "category_name"])

product_category_pairs, products_with_no_category = get_product_category_pairs(products_df, categories_df)

product_category_pairs.show()
products_with_no_category.show()
