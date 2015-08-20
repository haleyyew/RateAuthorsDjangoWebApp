class CreateBlogs < ActiveRecord::Migration
  def change
    create_table :blogs do |t|
      t.string :title
      t.string :url
      t.integer :ratings

      t.timestamps null: false
    end
  end
end
