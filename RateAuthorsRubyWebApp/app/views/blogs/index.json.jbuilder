json.array!(@blogs) do |blog|
  json.extract! blog, :id, :title, :url, :ratings
  json.url blog_url(blog, format: :json)
end
