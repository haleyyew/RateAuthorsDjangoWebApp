class Blog < ActiveRecord::Base
  belongs_to :author      #ADDED: association
end
