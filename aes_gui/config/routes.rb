Rails.application.routes.draw do
  root 'aes#home'
  post 'aes/upload'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
