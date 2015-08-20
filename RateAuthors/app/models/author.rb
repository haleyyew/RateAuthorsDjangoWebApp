class Author < ActiveRecord::Base
  has_many :blogs   #ADDED: association
end
